import unittest

from list_exercise import corn_exercise


class ListFunctionTest(unittest.TestCase):
    def test_total_function(self):
        number = [15, 20, 25, 20, 10, 5]
        expected = corn_exercise.total(number)
        self.assertEqual(expected, 95)

    def test_product_function(self):
        number = [15, 20, 25, 20, 10, 5]
        expected = corn_exercise.multiplication(number)
        self.assertEqual(expected, 7500000)

    def test_largestNumber_function(self):
        number = [15, 20, 25, 20, 10, 5, 70]
        expected = corn_exercise.largest_number(number)
        self.assertEqual(expected, 70)

    def test_smallestNumber_function(self):
        number = [15, 20, 25, 20, 10, 5, 70]
        expected = corn_exercise.smallest_number(number)
        self.assertEqual(expected, 5)

    def test_removal_of_duplicate_function(self):
        number = {15, 20, 25, 20, 10, 5, 70, 70, 25, 10}
        expected = {5, 70, 10, 15, 20, 25}
        actual = corn_exercise.remove_duplicate(number)
        self.assertEqual(actual, expected)
