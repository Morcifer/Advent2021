from unittest import TestCase

from src.day7_crabs import day7_parser, find_best_location_and_fuel, non_linear_fuel
from src.utilities import load_data


class TestDay7(TestCase):
    def test_find_best_location_linear_fuel(self):
        positions = load_data(7, day7_parser, "../data")[0]
        location, fuel = find_best_location_and_fuel(positions, linear=True)
        self.assertEqual(342, location)
        self.assertEqual(325528, fuel)

    def test_find_best_location_non_linear_fuel(self):
        positions = load_data(7, day7_parser, "../data")[0]
        location, fuel = find_best_location_and_fuel(positions, linear=False)
        self.assertEqual(460, location)
        self.assertEqual(85015836, fuel)

    def test_non_linear_fuel(self):
        self.assertEqual(66, non_linear_fuel(16, 5))
        self.assertEqual(10, non_linear_fuel(1, 5))
        self.assertEqual(6, non_linear_fuel(2, 5))
        self.assertEqual(15, non_linear_fuel(0, 5))
        self.assertEqual(1, non_linear_fuel(4, 5))
        self.assertEqual(3, non_linear_fuel(7, 5))
        self.assertEqual(45, non_linear_fuel(14, 5))
