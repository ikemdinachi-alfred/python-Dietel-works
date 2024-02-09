import unittest

from TestFolder.TDD import functions

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = functions.add(10, 5)
        result = functions.add(150, 500)
        result = functions.add(25, -24)
        self.assertEqual(result, 1)

    def test_subtraction(self):
        result = functions.subtraction(35, -25)
        self.assertEqual(result, 60)

def test_square_root(self):
        expected = functions.square_root(5)
        expected = functions.square_root(25)
        self.assertEqual(expected, 625)
