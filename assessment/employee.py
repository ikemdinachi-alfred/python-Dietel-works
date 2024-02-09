class Employee():

    def __init__(self, emp_id, emp_name, hourly_rate, number_of_hours_worked,emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.number_of_hours_worked = number_of_hours_worked;
        self.hourly_rate = 10;
        self.emp_department = emp_department;


def set_number_of_hours_worked(self, number_of_hours_worked):
    if 0 < number_of_hours_worked <= 200:
     self.number_of_hours_worked = number_of_hours_worked
    else: print("Invalid number of hours worked")
def get_number_of_hours_worked(self):
    return self.number_of_hours_worked;

def get_hourly_rate(self):
    return self.hourly_rate;


def set_emp_id(self, emp_id: int):
    self.emp_id = emp_id;
def get_emp_id(self):
    return self.emp_id

def set_emp_name(self, emp_name: str):
    self.emp_name = emp_name

    def get_emp_name(self):
        return self.emp_name

def get_salary(self):
    return self.number_of_hours_worked * self.hourly_rate;

def set_emp_department(self, emp_department):
    self.emp_department = emp_department;

def get_emp_department(self):
    return self.emp_department
