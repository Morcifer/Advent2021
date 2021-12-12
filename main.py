from functools import reduce
from statistics import median

from src.day10_paranthesis import day10_parser, find_all_corrupted_scores, find_all_autocorrect_scores
from src.day11_flashes import day11_parser, simulate_all_steps_of_map, find_first_simultaneous_flash
from src.day12_graph import day12_parser, find_all_paths
from src.day1_calculators import count_increases, rolling_horizon, day1_parser
from src.day2_commands import calculate_final_location, day2_parser
from src.day3_binary import day3_parser, calculate_gamma_and_epsilon, calculate_oxygen_and_scrubber
from src.day4_bingo import load_bingo_data, find_winning_board, find_losing_board
from src.day5_lines import day5_parser, calculate_final_grid
from src.day6_FIESH import day6_parser, simulate_fish, simulate_fish_better
from src.day7_crabs import day7_parser, find_best_location_and_fuel
from src.day8_digits import day8_parser, count_digits_in_output, get_number
from src.day9_lava import day9_parser, find_high_spots, find_basins_values
from src.utilities import load_data


def day1_1() -> int:
    data = load_data(1, day1_parser, "data")
    return count_increases(data)


def day1_2() -> int:
    data = load_data(1, day1_parser, "data")
    return count_increases(rolling_horizon(data))


def day2_1() -> int:
    commands = load_data(2, day2_parser, "data")
    x, y = calculate_final_location(commands, "move")
    return x * y


def day2_2() -> int:
    commands = load_data(2, day2_parser, "data")
    x, y = calculate_final_location(commands, "move_with_aim")
    return x * y


def day3_1() -> int:
    diagnostics = load_data(3, day3_parser, "data")
    gamma, epsilon = calculate_gamma_and_epsilon(diagnostics)
    return gamma * epsilon


def day3_2() -> int:
    diagnostics = load_data(3, day3_parser, "data")
    oxygen, scrubber = calculate_oxygen_and_scrubber(diagnostics)
    return oxygen * scrubber


def day4_1() -> int:
    numbers, boards = load_bingo_data("data")
    winning_board, number = find_winning_board(numbers, boards)
    return winning_board.score() * number


def day4_2() -> int:
    numbers, boards = load_bingo_data("data")
    losing_board, number = find_losing_board(numbers, boards)
    return losing_board.score() * number


def day5_1() -> int:
    lines = load_data(5, day5_parser, "data")
    final_grid = calculate_final_grid(lines, filter_diagonal=True)
    return final_grid.get_high_risk_count()


def day5_2() -> int:
    lines = load_data(5, day5_parser, "data")
    final_grid = calculate_final_grid(lines, filter_diagonal=False)
    return final_grid.get_high_risk_count()


def day6_1() -> int:
    fish = load_data(6, day6_parser, "data")[0]
    fish = simulate_fish_better(fish, time=80)
    return fish


def day6_2() -> int:
    fish = load_data(6, day6_parser, "data")[0]
    fish = simulate_fish_better(fish, time=256)
    return fish


def day7_1() -> int:
    positions = load_data(7, day7_parser, "data")[0]
    location, fuel = find_best_location_and_fuel(positions, linear=True)
    return fuel


def day7_2() -> int:
    positions = load_data(7, day7_parser, "data")[0]
    location, fuel = find_best_location_and_fuel(positions, linear=False)
    return fuel


def day8_1() -> int:
    data = load_data(8, day8_parser, "data")
    number_of_digits = count_digits_in_output(data)
    return number_of_digits


def day8_2() -> int:
    data = load_data(8, day8_parser, "data")
    numbers = [get_number(datum) for datum in data]
    return sum(numbers)


def day9_1() -> int:
    heights = load_data(9, day9_parser, "data")
    high_spots, high_spots_values = find_high_spots(heights)
    return sum(high_spots_values) + len(high_spots_values)


def day9_2() -> int:
    heights = load_data(9, day9_parser, "data")
    basins_values = find_basins_values(heights)
    basins_values = sorted(basins_values)
    return reduce((lambda x, y: x * y), basins_values[-3:])


def day10_1() -> int:
    data = load_data(10, day10_parser, "data")
    scores = find_all_corrupted_scores(data)
    return sum(scores)


def day10_2() -> int:
    data = load_data(10, day10_parser, "data")
    scores = find_all_autocorrect_scores(data)
    return median([s for s in scores if s != -1])


def day11_1() -> int:
    data = load_data(11, day11_parser, "data")
    flashes = simulate_all_steps_of_map(data)
    return flashes


def day11_2() -> int:
    data = load_data(11, day11_parser, "data")
    step = find_first_simultaneous_flash(data)
    return step


def day12_1() -> int:
    edges = load_data(12, day12_parser, "data")
    paths = find_all_paths(edges, once_at_most=True)
    return len(paths)


def day12_2() -> int:
    edges = load_data(12, day12_parser, "data")
    paths = find_all_paths(edges, once_at_most=False)
    return len(paths)


if __name__ == '__main__':
    print(f"Day 1 result 1: {day1_1()}")
    print(f"Day 1 result 2: {day1_2()}")
    print(f"Day 2 result 1: {day2_1()}")
    print(f"Day 2 result 2: {day2_2()}")
    print(f"Day 3 result 1: {day3_1()}")
    print(f"Day 3 result 2: {day3_2()}")
    print(f"Day 4 result 1: {day4_1()}")
    print(f"Day 4 result 2: {day4_2()}")
    print(f"Day 5 result 1: {day5_1()}")
    print(f"Day 5 result 2: {day5_2()}")
    print(f"Day 6 result 1: {day6_1()}")
    print(f"Day 6 result 2: {day6_2()}")
    print(f"Day 7 result 1: {day7_1()}")
    print(f"Day 7 result 2: {day7_2()}")
    print(f"Day 8 result 1: {day8_1()}")
    print(f"Day 8 result 2: {day8_2()}")
    print(f"Day 9 result 1: {day9_1()}")
    print(f"Day 9 result 2: {day9_2()}")
    print(f"Day 10 result 1: {day10_1()}")
    print(f"Day 10 result 2: {day10_2()}")
    print(f"Day 11 result 1: {day11_1()}")
    print(f"Day 11 result 2: {day11_2()}")
    print(f"Day 12 result 1: {day12_1()}")
    # print(f"Day 12 result 2: {day12_2()}")  # Run-time too long because I'm lazy
