import os
import shutil
from pathlib import Path
from custom_types import ResultList


def copy_files(path: str, data: ResultList) -> None:
    directory = Path(path)
    print(f"PATH {path}", directory.resolve())
    if not directory.exists():
        path_root_dir = str(directory.resolve())
        print(f"Create destination directory: \"{path_root_dir}\"")
        try:
            os.mkdir(path_root_dir)
        except Exception as e:
            print(f"{e}")

    for item in data:
        if not item.get("is_dir"):
            name = item.get("name")
            file_path = item.get("path")
            info = name.split(".")
            if len(info) == 1:
                print(f"File <{info[0]}> without extension.")
            else:
                ext = info[1]
                directory = Path(path, ext)
                path_ext_dir = str(directory.resolve())

                try:
                    if not directory.exists():
                        print(
                            f"Create extension directory: \"{path_ext_dir}\"")
                        os.mkdir(path_ext_dir)

                    file_dist_path = str(Path(path_ext_dir, name).resolve())
                    if not os.path.isfile(file_dist_path):
                        shutil.copyfile(file_path, file_dist_path)
                        print("Copy file:", file_dist_path)
                    else:
                        print("Duplicate file:", file_dist_path)

                except Exception as e:
                    print(f"{e}")
