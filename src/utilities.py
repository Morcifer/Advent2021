from typing import List, TypeVar, Callable


ResultType = TypeVar('ResultType')


def load_data(day: int, parser: Callable[[str], ResultType], data_folder: str) -> List[ResultType]:
    file_name = f"{data_folder}/day{day}_data.txt"

    with open(file_name) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    mat = []

    for line in content:
        s = line.split(' ')
        mat.append(parser(s))

    return mat
