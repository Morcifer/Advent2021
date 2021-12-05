from unittest import TestCase

from src.day3_binary import calculate_gamma_and_epsilon, day3_parser, calculate_oxygen_and_scrubber
from src.utilities import load_data


class TestDay3(TestCase):
    def test_calculate_gamma_and_epsilon(self):
        diagnostics = load_data(3, day3_parser, "../data")
        result = calculate_gamma_and_epsilon(diagnostics)
        self.assertEqual((281, 3814), result)
        self.assertEqual(1071734, result[0] * result[1])

    def test_calculate_oxygen_and_scrubber(self):
        diagnostics = load_data(3, day3_parser, "../data")
        result = calculate_oxygen_and_scrubber(diagnostics)
        self.assertEqual((1679, 3648), result)
        self.assertEqual(6124992, result[0] * result[1])