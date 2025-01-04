from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.document import Document
from listing_files import directory_check


class RequiredStringValidator(Validator):
    def __init__(self, as_path: bool):
        self.__as_path = as_path
        super().__init__()

    def validate(self, document: Document) -> None:
        text = document.text.strip()
        if not text:  # Check for empty or whitespace-only strings
            raise ValidationError(
                message="This argument is required.", cursor_position=0)

        is_exist, path = directory_check(text)
        if self.__as_path and not is_exist:
            raise ValidationError(
                message=f"Source dir not exist: {path}")


def get_input(prompt_text: str, default: str | None = None, required: bool = False, as_path: bool = False) -> str | None:
    """
    Prompts the user for input with optional validation and default value.
    """
    if default is not None:
        display_default = f"[default: {default}]"
        pre_fill = str(default)  # default must be string for prompt
    elif required:
        display_default = "(required)"
        pre_fill = ""
    else:
        display_default = ""
        pre_fill = ""

    validator = RequiredStringValidator(as_path) if required else None

    try:
        user_input = prompt(f"{prompt_text} {display_default}: ",
                            default=pre_fill, validator=validator)
        if not user_input.strip() and required:
            raise ValueError("Input is required.")
        elif not user_input.strip() and default is not None:
            return default
        return user_input

    except KeyboardInterrupt:
        print("\nInput cancelled.")
        return None
