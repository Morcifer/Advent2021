from collections import Counter
from typing import List, Callable


def day20_parser(s: List[str]) -> str:
    return s[0]


def split_data(data: List[str]) -> (str, List[str]):
    enhancement = ""
    image = []
    sep_found = False

    for s in data:
        if s == "":
            sep_found = True
            continue

        if sep_found:
            image.append(s)
        else:
            enhancement = enhancement + s

    return enhancement, image


def enhance(enhancement: str, image: List[str]) -> List[str]:
    # print_image(image)

    infinite_space = 5

    height = len(image) + infinite_space * 2
    width = len(image[0]) + infinite_space * 2

    edge = image[0][0]
    empty = "".join([edge for _ in range(width)])
    bigger_image = [empty] * (infinite_space * 2)
    bigger_image[infinite_space:-infinite_space] = [edge * infinite_space + s + edge * infinite_space for s in image]

    # print_image(bigger_image)

    enhanced_image = []

    for i in range(1, height - 1):
        new_row = ""
        for j in range(1, width - 1):
            sub_image = bigger_image[i-1][j-1:j+2] + bigger_image[i][j-1:j+2] + bigger_image[i+1][j-1:j+2]
            binary_str = sub_image.replace(".", "0").replace("#", "1")
            binary = int(binary_str, 2)
            new_row = new_row + enhancement[binary]
        enhanced_image.append(new_row)

    # print_image(enhanced_image)

    return enhanced_image


def count_lights(image: List[str]) -> int:
    return Counter("".join(image))["#"]


def print_image(image: List[str]) -> None:
    for row in image:
        print(row)
    print()
