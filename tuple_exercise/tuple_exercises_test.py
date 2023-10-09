import unittest

import tuple_exercise


class TestForTuples(unittest.TestCase):
    def test_reverse_number(self):
        number = (10, 20, 30, 40, 50)
        expected = (50, 40, 30, 20, 10)
        result = (tuple_exercise.reverse_tuple(number))
        self.assertEqual(result, expected)

    def test_swaping_first_to_last_tuple(self):
        number = ("orange", [10, 20, 30], [5, 15, 25])
        expected = (0, 20), (1, 25)
        rersult = tuple_exercise.swaping_the_first_with_last(number)
        self.assertEqual(rersult, expected)


