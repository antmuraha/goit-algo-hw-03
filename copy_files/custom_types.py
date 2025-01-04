from typing import TypedDict, List


class ResultItem(TypedDict):
    level: int
    name: str
    path: str
    is_dir: bool


ResultList = List[ResultItem]
