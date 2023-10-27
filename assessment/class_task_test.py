import unittest
from assessment import class_task


class TestListFunction(unittest.TestCase):
    def test_validity_list(self):
        actual = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected = class_task.list_of_numbers(actual)
        self.assertEqual(expected, actual)

    def test_odd_numbers(self):
        actual = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        result = class_task.odd_number_check(actual)
        self.assertEqual(result, expected)

    def test_odd_numbers_double(self):
        actual = list(range(1, 21))
        expected = [2, 6, 10, 14, 18, 22, 26, 30, 34, 36]
        result = class_task.doubling_number_in_list(actual)
        self.assertEqual(result, expected)

    def test_list_change_some_items_to_zero(self):
        actual = list(range(1, 21))
        expected = [2, 6, 10, 14, 0, 0, 0, 0, 34, 36]
        result = class_task.exercise4(actual)
        self.assertEqual(result, expected)

    def test_function_can_concatenate_two_list(self):
        list1 = ['w', 'a', 'th', 'xplo']
        list2 = ['e', 're', 'e', 'rers']
        list3 = ['we', 'are', 'the', 'xplorers']
        self.assertEqual(class_task.exercise5(list1, list2), list3)
