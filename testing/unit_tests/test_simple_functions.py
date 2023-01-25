from unittest import TestCase, skip, skipUnless
from decimal import Decimal
from datetime import datetime, date

from testing.simple_functions import sum_two_numbers


class SimpleFunctionsTests(TestCase):
    _today = datetime.now().date()

    def test_sum_two_numbers(self):
        # test_cases = [
        #     ((4, 5), 9),
        #     (('4', 5), 9),
        #     ((None, 5), 9),
        #     ((Decimal(5), 5.1), 10.1),
        # ]
        # for (a, b), result in test_cases:
        #     with self.subTest(result=result):
        #         self.assertEqual(sum_two_numbers(a, b), result)

        self.assertEqual(sum_two_numbers(4, 5), 9)
        self.assertIsNone(sum_two_numbers('a', 5))
        # self.assertRaises(TypeError, lambda: sum_two_numbers(None, 5))
        # self.assertRaises(TypeError, lambda: sum_two_numbers(Decimal(5), 5.1))

    @skipUnless(_today >= date(2023, 2, 25), "Not created functionality")
    def test_subtract_numbers(self):
        subtract_number(5, 6)
