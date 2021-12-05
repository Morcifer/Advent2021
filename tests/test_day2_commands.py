from unittest import TestCase

from src.day2_commands import calculate_final_location, Command, day2_parser
from src.utilities import load_data


class TestDay2(TestCase):
    def test_calculate_final_location_with_move(self):
        commands = load_data(2, day2_parser, "../data")

        result = calculate_final_location(commands, "move")
        self.assertEqual((2024, 717), result)
        self.assertEqual(1451208, result[0] * result[1])

    def test_calculate_final_location_with_move_with_aim(self):
        commands = load_data(2, day2_parser, "../data")

        result = calculate_final_location(commands, "move_with_aim")
        self.assertEqual((2024, 800465), result)
        self.assertEqual(1620141160, result[0] * result[1])

    def test_command_move(self):
        self.assertEqual((5, 0), Command("forward", 5).move(0, 0))
        self.assertEqual((5, 5), Command("down", 5).move(5, 0))
        self.assertEqual((13, 5), Command("forward", 8).move(5, 5))
        self.assertEqual((13, 2), Command("up", 3).move(13, 5))
        self.assertEqual((13, 10), Command("down", 8).move(13, 2))
        self.assertEqual((15, 10), Command("forward", 2).move(13, 10))

    def test_command_move_with_aim(self):
        self.assertEqual((5, 0, 0), Command("forward", 5).move_with_aim(0, 0, 0))
        self.assertEqual((5, 0, 5), Command("down", 5).move_with_aim(5, 0, 0))
        self.assertEqual((13, 40, 5), Command("forward", 8).move_with_aim(5, 0, 5))
        self.assertEqual((13, 40, 2), Command("up", 3).move_with_aim(13, 40, 5))
        self.assertEqual((13, 40, 10), Command("down", 8).move_with_aim(13, 40, 2))
        self.assertEqual((15, 60, 10), Command("forward", 2).move_with_aim(13, 40, 10))
