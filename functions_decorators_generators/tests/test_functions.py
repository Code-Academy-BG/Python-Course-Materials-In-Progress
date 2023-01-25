from unittest import TestCase

from functions_decorators_generators.functions import power
from functions_decorators_generators.homework import get_min_of_three_members


class FunctionsTests(TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 4), 16)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(4, 2), 16)
        self.assertEqual(power(4, 3), 64)
        self.assertEqual(power(8, 2), 64)
        self.assertEqual(power(9, 2), 81)

    def test_without_function(self):
        self.assertEqual(3 + 5, 8)
        self.assertIsNone(None)
        self.assertFalse(False)

        dict_to_compare_one = {
            "one": 1,
            "two": 2,
        }

        dict_to_compare_two = {
            "two": 2,
            "one": 1,
        }
        self.assertDictEqual(dict_to_compare_one, dict_to_compare_two)
        self.assertAlmostEqual(5.1, 5.09999999)

    def test_get_min_of_three_members(self):
        self.assertEqual(get_min_of_three_members(3, 5, 6), 3)
        self.assertEqual(get_min_of_three_members(7, 5, 6), 5)
        self.assertEqual(get_min_of_three_members(3, 3, 3), 3)
