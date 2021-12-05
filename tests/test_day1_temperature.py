from unittest import TestCase

from src.day1_calculators import count_increases, rolling_horizon, day1_parser
from src.utilities import load_data


class TestDay1(TestCase):
    def test_count_increases(self):
        data = load_data(1, day1_parser, "../data")
        result = count_increases(data)
        self.assertEqual(1583, result)

    def test_rolling_horizon(self):
        data = load_data(1, day1_parser, "../data")
        rolling_data = rolling_horizon(data)
        result = count_increases(rolling_data)
        self.assertEqual(1627, result)
