from unittest import TestCase

from src.day16_bits import day16_parser, parse


class TestDay8(TestCase):
    def test_parse_1(self):
        data = day16_parser(["8A004A801A8002F478"])
        result = []
        parse(data, result)
        self.assertEqual(16, sum(result))

    def test_parse_2(self):
        data = day16_parser(["620080001611562C8802118E34"])
        result = []
        parse(data, result)
        self.assertEqual(12, sum(result))

    def test_parse_3(self):
        data = day16_parser(["C0015000016115A2E0802F182340"])
        result = []
        parse(data, result)
        self.assertEqual(23, sum(result))

    def test_parse_4(self):
        data = day16_parser(["A0016C880162017C3686B18A3D4780"])
        result = []
        parse(data, result)
        self.assertEqual(31, sum(result))
