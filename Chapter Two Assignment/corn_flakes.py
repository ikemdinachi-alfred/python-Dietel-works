

employee_name = str(input('Enter Employee Name:  '))
hour_worked = float(input('Enter Hours Worked: $'))
pay_rate = float(input('Enter per rate per hour: $ '))
print('\n')
gross_pay = pay_rate * hour_worked
federal_withholding = gross_pay * 0.20
state_withholding = gross_pay * 0.09

print(f' {employee_name} payroll statement for the month of April')
print(f' Gross pay: ${gross_pay}  \n Deductions:  ')

print(f' Federal Withholding (20.0%): $ {federal_withholding} \n State Withholding (9.0%): $ {state_withholding} \n Total Deduction: ${federal_withholding + state_withholding} \n Net pay: ${gross_pay - state_withholding -federal_withholding}')


