from unittest import TestCase

from src.day8_digits import day8_parser, count_digits_in_output, get_number
from src.utilities import load_data


class TestDay8(TestCase):
    def test_count_digits_in_output(self):
        data = load_data(8, day8_parser, "../data")
        number_of_digits = count_digits_in_output(data)
        self.assertEqual(543, number_of_digits)

    def test_get_number(self):
        data = load_data(8, day8_parser, "../data")
        numbers = [get_number(datum) for datum in data]
        self.assertEqual(994266, sum(numbers))
