from unittest import TestCase

from src.day6_FIESH import day6_parser, simulate_fish, simulate_fish_better
from src.utilities import load_data


class TestDay6(TestCase):
    def test_fish_population(self):
        fish = load_data(6, day6_parser, "../data")[0]
        fish = simulate_fish(fish, time=80)
        self.assertEqual(363101, fish)

    def test_better_fish_population(self):
        fish = load_data(6, day6_parser, "../data")[0]
        fish = simulate_fish_better(fish, time=80)
        self.assertEqual(363101, fish)

    def test_better_fish_population_long(self):
        fish = load_data(6, day6_parser, "../data")[0]
        fish = simulate_fish_better(fish, time=256)
        self.assertEqual(1644286074024, fish)
