from typing import List


class BingoBoard:
    numbers: List[List[int]]

    def __init__(self, five_lines: List[str]):
        self.numbers = []
        for line in five_lines:
            five_numbers = line.split()
            self.numbers.append([int(s) for s in five_numbers])

    def mark_number(self, number: int):
        for i in range(5):
            for j in range(5):
                if self.numbers[i][j] == number:
                    self.numbers[i][j] = -1

    def is_bingo(self) -> bool:
        for i in range(5):
            row_bingo = True
            for j in range(5):
                row_bingo = row_bingo and self.numbers[i][j] == -1

            if row_bingo:
                return True

        for j in range(5):
            column_bingo = True
            for i in range(5):
                column_bingo = column_bingo and self.numbers[i][j] == -1

            if column_bingo:
                return True

        return False

    def score(self) -> int:
        return sum(sum(value for value in row if value >= 0) for row in self.numbers)


def load_bingo_data(data_folder: str) -> (List[int], List[BingoBoard]):
    file_name = f"{data_folder}/day4_data.txt"

    with open(file_name) as f:
        content = f.readlines()

    first = True

    numbers = []
    boards = []

    this_board_lines = []
    line_index = 0

    for line in [l.strip() for l in content]:
        if line == "":
            continue

        if first:
            numbers = [int(s) for s in line.split(',')]
            first = False
        else:
            this_board_lines.append(line)
            line_index += 1
            if line_index == 5:
                boards.append(BingoBoard(this_board_lines))

                this_board_lines = []
                line_index = 0

    return numbers, boards


def find_winning_board(numbers: List[int], boards: List[BingoBoard]) -> (BingoBoard, int):
    for number in numbers:
        for board in boards:
            board.mark_number(number)
            if board.is_bingo():
                return board, number


def find_losing_board(numbers: List[int], boards: List[BingoBoard]) -> (BingoBoard, int):
    number_of_boards = len(boards)
    winning_boards = []

    for number in numbers:
        for board in boards:
            board.mark_number(number)
            if board.is_bingo() and board not in winning_boards:
                winning_boards += [board]
                if len(winning_boards) == number_of_boards:
                    return board, number

    return None, -1
