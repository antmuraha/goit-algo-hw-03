from pathlib import Path
from custom_types import ResultList

DEFAULT_INDENT = "    "


def directory_check(path: str) -> tuple[bool, str]:
    directory = Path(path)

    if not directory.exists():
        return (False, str(directory.resolve()))

    if not directory.is_dir():
        return (False, str(directory.resolve()))

    return (True, str(directory.resolve()))


def listing_files(result: ResultList, path: str = ".", level: int = 0) -> None:
    """
    This function takes a directory path and returns a list
    of all subdirectories and files
    Example:
        # List for results\n
        result = []

        # Current dir\n
        listing_files(result, ".")

        # Relative path to some_dir\n
        listing_files(result, "some_dir")

        # Absolutely path to some_dir\n
        listing_files(result, "/absolutely-to/some_dir")
    """

    directory = Path(path)
    if level == 0 and not directory.exists():
        raise Exception(f"The directory {directory.resolve()} does not exist")

    if level == 0 and directory.is_file():
        raise Exception(f"This {directory.resolve()} is a file")

    if level == 0:
        result.append({
            "level": 0,
            "name": directory.name,
            "path": str(directory.resolve()),
            "is_dir": True
        })
        listing_files(result, str(directory.resolve()), level + 1)
        return

    for item in directory.iterdir():
        is_dir = item.is_dir()
        result.append({
            "level": level,
            "name": item.name,
            "path": str(directory.resolve()) if is_dir else str(Path(directory, item.name).resolve()),
            "is_dir": is_dir
        })
        if is_dir:
            listing_files(result, str(item.resolve()), level + 1)

    return None
