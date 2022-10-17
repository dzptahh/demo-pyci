from unittest import TestCase
from statistics import *
from math import sqrt


class StatisticsTest(TestCase):

    def test_variance_typical_values(self):
        """variance of typical values"""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_throws_exception(self):
        """variance of an empty list should raise an exception"""
        with self.assertRaises(ValueError):
            var = variance([])

    def test_standard_deviation(self):
        """standard deviation should raise correct value"""
        self.assertEqual(0.0, stdev([10.0, 10.0]))
        self.assertEqual(sqrt(2.0), stdev([1, 2, 3, 4, 5]))
        self.assertEqual(sqrt(8.0), stdev([10, 2, 8, 4, 6]))


if __name__ == '__main__':
    import unittest

    unittest.main(verbosity=1)
