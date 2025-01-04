from completer import get_input
from listing_files import listing_files, directory_check
from custom_types import ResultList
from copy_files import copy_files


def main() -> None:
    print("Welcome to the File Copy Assistant!")

    while True:

        arg1 = get_input("Enter source path", required=True, as_path=True)
        if arg1 is None:
            return
        _, path = directory_check(arg1)
        print(f"Source folder: {path}")

        arg2 = get_input("Enter destination path", default="dist")
        if arg2 is None:
            return

        print(f"Destination path: {arg2}")

        arg3 = get_input("Is this OK? (Yes)", required=True)
        is_ok = ["yes", "y"]
        if not arg3 or arg3.lower() not in is_ok:
            return

        print(f"arg1: {arg1}, arg2: {arg2}", arg3)

        result: ResultList = []
        listing_files(result, arg1)
        copy_files(arg2, result)
        return


if __name__ == "__main__":
    main()
