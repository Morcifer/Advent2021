from src.day1_calculators import count_increases, rolling_horizon, day1_parser
from src.day2_commands import calculate_final_location, day2_parser
from src.day3_binary import day3_parser, calculate_gamma_and_epsilon, calculate_oxygen_and_scrubber
from src.day4_bingo import load_bingo_data, find_winning_board, find_losing_board
from src.day5_lines import day5_parser, calculate_final_grid
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
    print(f"Day 5 result 1: {day5_2()}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
