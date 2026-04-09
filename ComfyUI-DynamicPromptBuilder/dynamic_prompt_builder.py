import random
import re

class DynamicPromptBuilder:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template": ("STRING", {"multiline": True, "dynamicPrompts": False}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "build_prompt"
    CATEGORY = "utils"

    def build_prompt(self, template, seed, **kwargs):
        rng = random.Random(seed)
        result = template
        
        matches = set(re.findall(r'\{([^}]+)\}', template))
        
        for match in matches:
            parts = [p for p in match.split('|') if p]
            if not parts:
                result = result.replace(f"{{{match}}}", "")
                continue

            chosen_part = rng.choice(parts)
            val = kwargs.get(chosen_part, "")
            
            if isinstance(val, str) and val.strip():
                lines = [line.strip() for line in val.split("\n") if line.strip()]
                if lines:
                    chosen = rng.choice(lines)
                    result = result.replace(f"{{{match}}}", chosen)
                else:
                    result = result.replace(f"{{{match}}}", chosen_part)
            else:
                result = result.replace(f"{{{match}}}", chosen_part)
                
        return (result,)
