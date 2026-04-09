import random
import re
import os
import folder_paths

class ResolutionPoolString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "dynamicPrompts": False}),
                "resolutions": ("STRING", {"multiline": True, "dynamicPrompts": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "apply_resolutions"
    CATEGORY = "utils"

    def apply_resolutions(self, text, resolutions):
        res_lines = [r.strip() for r in resolutions.split('\n') if r.strip()]
        if not res_lines:
            return (text,)
            
        joined_res = ','.join(res_lines)
        text_lines = text.split('\n')
        
        out_lines = []
        for line in text_lines:
            clean_line = line.strip()
            if clean_line:
                out_lines.append(f"{line} --res {joined_res}")
            else:
                out_lines.append(line)
                
        return ("\n".join(out_lines),)

class DynamicPromptBuilder:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template": ("STRING", {"multiline": True, "dynamicPrompts": False}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING", "INT", "INT")
    RETURN_NAMES = ("prompt", "width", "height")
    FUNCTION = "build_prompt"
    CATEGORY = "utils"

    def build_prompt(self, template, seed, **kwargs):
        rng = random.Random(seed)
        result = template
        
        matches = set(re.findall(r'\{([^}]+)\}', template))
        
        for match in matches:
            inner = match
            sample_count = 1
            if "$$" in inner:
                count_str, inner_trimmed = inner.split("$$", 1)
                try:
                    sample_count = int(count_str.strip())
                    inner = inner_trimmed
                except ValueError:
                    pass

            parts = [p.strip() for p in inner.split('|') if p.strip()]
            if not parts:
                result = result.replace(f"{{{match}}}", "")
                continue

            weights = []
            clean_parts = []
            for p in parts:
                if "::" in p:
                    w_str, val = p.split("::", 1)
                    try:
                        weights.append(float(w_str.strip()))
                        clean_parts.append(val.strip())
                    except ValueError:
                        weights.append(1.0)
                        clean_parts.append(p)
                else:
                    weights.append(1.0)
                    clean_parts.append(p)

            chosen_items = []
            pool = list(clean_parts)
            w = list(weights)
            k = min(sample_count, len(pool))
            
            for _ in range(k):
                if sum(w) <= 0:
                    break
                chosen = rng.choices(pool, weights=w, k=1)[0]
                idx = pool.index(chosen)
                chosen_items.append(chosen)
                pool.pop(idx)
                w.pop(idx)
            
            final_replacements = []
            for c_part in chosen_items:
                val = kwargs.get(c_part, "")
                if isinstance(val, str) and val.strip():
                    lines = [line.strip() for line in val.split("\n") if line.strip()]
                    if lines:
                        final_replacements.append(rng.choice(lines))
                    else:
                        final_replacements.append(c_part)
                else:
                    final_replacements.append(c_part)
            
            if final_replacements:
                replacement_str = ", ".join(final_replacements)
                result = result.replace(f"{{{match}}}", replacement_str)
            else:
                result = result.replace(f"{{{match}}}", "")

        base_wildcards = os.path.join(folder_paths.base_path, "wildcards")
        local_wildcards = os.path.join(os.path.dirname(os.path.realpath(__file__)), "wildcards")

        loop_count = 0
        while loop_count < 5:
            wildcard_matches = set(re.findall(r'__([a-zA-Z0-9_\-]+)__', result))
            if not wildcard_matches:
                break
                
            for w_match in wildcard_matches:
                file_name = f"{w_match}.txt"
                found_lines = []
                
                paths_to_check = [
                    os.path.join(base_wildcards, file_name),
                    os.path.join(local_wildcards, file_name)
                ]
                
                for p in paths_to_check:
                    if os.path.isfile(p):
                        try:
                            with open(p, 'r', encoding='utf-8') as f:
                                lines = [line.strip() for line in f.readlines() if line.strip()]
                                if lines:
                                    found_lines = lines
                                    break
                        except Exception:
                            pass
                            
                if found_lines:
                    chosen_line = rng.choice(found_lines)
                    result = result.replace(f"__{w_match}__", chosen_line)
                else:
                    result = result.replace(f"__{w_match}__", w_match)
                    
            loop_count += 1

        width = 1408
        height = 1408

        match_res = re.search(r'--res\s*([\d\s,xX]+)', result)
        if match_res:
            res_str = match_res.group(1)
            options = [o.strip() for o in res_str.split(',') if o.strip()]
            if options:
                chosen_res = rng.choice(options)
                parts = re.split(r'[xX]', chosen_res)
                if len(parts) == 2:
                    try:
                        width = int(parts[0].strip())
                        height = int(parts[1].strip())
                    except ValueError:
                        pass
            
            result = re.sub(r'\s*--res\s*[\d\s,xX]+', '', result)

        result = re.sub(r'\s+', ' ', result).strip()
                
        preview_string = f"Prompt:\n{result}\n\nResolution: {width} x {height}"
        return {"ui": {"text": [preview_string]}, "result": (result, width, height)}
