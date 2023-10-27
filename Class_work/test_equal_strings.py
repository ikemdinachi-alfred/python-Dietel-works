import unittest

from Class_work import equal_strings


class Test(unittest.TestCase):
    def test_equal_strings(self):
        value = "love"
        value1 = "evol"
        result = equal_strings.equal_strings(value, value1)

        self.assertTrue(result)
