from unittest import TestCase

from src.day5_lines import day5_parser, calculate_final_grid
from src.utilities import load_data


class TestDay5(TestCase):
    def test_calculate_high_risk_count_filter_diagonal(self):
        lines = load_data(5, day5_parser, "../data")
        final_grid = calculate_final_grid(lines, filter_diagonal=True)
        result = final_grid.get_high_risk_count()
        self.assertEqual(7380, result)

    def test_calculate_high_risk_count_keep_diagonal(self):
        lines = load_data(5, day5_parser, "../data")
        final_grid = calculate_final_grid(lines, filter_diagonal=False)
        result = final_grid.get_high_risk_count()
        self.assertEqual(21373, result)
