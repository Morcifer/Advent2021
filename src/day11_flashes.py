from typing import List, Set


def day11_parser(s: List[str]) -> List[int]:
    return [int(x) for x in s[0]]


map_size = 10


def simulate_all_steps_of_map(map: List[List[int]]) -> int:
    flashes = 0
    for step in range(100):
        flashes += simulate_single_map(map)
    return flashes


def find_first_simultaneous_flash(map: List[List[int]]) -> int:
    for step in range(100000000):
        flashes = simulate_single_map(map)
        if flashes == 100:
            return step + 1
    return -1


def simulate_single_map(map: List[List[int]]) -> int:
    flashed = set()
    to_flash = set()

    # Increment step
    for i in range(map_size):
        for j in range(map_size):
            increase_i_j_for_flashed(map, to_flash, i, j)

    while any(to_flash.difference(flashed)):
        now_i, now_j = to_flash.difference(flashed).pop()
        flashed.add((now_i, now_j))

        increase_i_j_for_flashed(map, to_flash, now_i - 1, now_j)
        increase_i_j_for_flashed(map, to_flash, now_i + 1, now_j)
        increase_i_j_for_flashed(map, to_flash, now_i, now_j - 1)
        increase_i_j_for_flashed(map, to_flash, now_i, now_j + 1)

        increase_i_j_for_flashed(map, to_flash, now_i - 1, now_j - 1)
        increase_i_j_for_flashed(map, to_flash, now_i - 1, now_j + 1)
        increase_i_j_for_flashed(map, to_flash, now_i + 1, now_j - 1)
        increase_i_j_for_flashed(map, to_flash, now_i + 1, now_j + 1)

    for now_i, now_j in flashed:
        map[now_i][now_j] = 0

    return len(flashed)


def increase_i_j_for_flashed(map: List[List[int]], to_flash: Set, i: int, j: int) -> None:
    if 0 <= i < map_size and 0 <= j < map_size:
        map[i][j] += 1
        if map[i][j] >= 10:
            to_flash.add((i, j))
