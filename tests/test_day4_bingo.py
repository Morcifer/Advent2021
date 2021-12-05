from unittest import TestCase

from src.day4_bingo import load_bingo_data, find_winning_board, find_losing_board


class TestDay4(TestCase):
    def test_find_winning_board(self):
        numbers, boards = load_bingo_data("../data")
        result = find_winning_board(numbers, boards)
        self.assertEqual(63424, result[0].score() * result[1])

    def test_find_losing_board(self):
        numbers, boards = load_bingo_data("../data")
        result = find_losing_board(numbers, boards)
        self.assertEqual(23541, result[0].score() * result[1])
