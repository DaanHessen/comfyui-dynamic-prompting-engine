from .dynamic_prompt_builder import DynamicPromptBuilder, ResolutionPoolString

NODE_CLASS_MAPPINGS = {
    "DynamicPromptBuilder": DynamicPromptBuilder,
    "ResolutionPoolString": ResolutionPoolString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DynamicPromptBuilder": "Dynamic Template Prompt Builder",
    "ResolutionPoolString": "String with Resolution Pool"
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
