import unittest
from assessment import employee
from assessment.employee import Employee


class EmployeeTest(unittest.TestCase):
    def test_set_number_of_hours_worked(self):
        Employee.set_number_of_hours_worked(200)
    self.assertEquals(200, employee.get_number_of_hours_worked())
