from .dynamic_prompt_builder import DynamicPromptBuilder

NODE_CLASS_MAPPINGS = {
    "DynamicPromptBuilder": DynamicPromptBuilder
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DynamicPromptBuilder": "Dynamic Template Prompt Builder"
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
