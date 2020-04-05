"""
weather.tests.test_utilities
----------------------------
Test the utils file from weather.utils
"""
import unittest
from decimal import Decimal

from weather.utils import decimal_range


class TestUtils(unittest.TestCase):

    def test_default_decimal_range(self):
        begin = Decimal(0)
        end = Decimal(1)
        default_decimal_range = []
        while begin < end:
            default_decimal_range.append(begin)
            begin += Decimal(str(0.1))
        test_decimal_range = list(decimal_range())

        self.assertListEqual(default_decimal_range, test_decimal_range)

    def test_decimal_range(self):
        begin = Decimal(4)
        end = Decimal(5)
        default_decimal_range = []
        while begin < end:
            default_decimal_range.append(begin)
            begin += Decimal(str(0.1))
        test_decimal_range = list(decimal_range(Decimal(4), Decimal(5)))

        self.assertListEqual(default_decimal_range, test_decimal_range)
