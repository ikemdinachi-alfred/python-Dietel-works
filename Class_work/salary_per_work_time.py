def teachers_salary(Teachers_name, period):
    if period >= 100:
        gross_salary = (period * 20) + (period - 100) * 25
    else:
        gross_salary = period * 20
    return print(f' Teacher: {Teachers_name}\n  period: {period}\n  Gross salary {gross_salary}')


print(teachers_salary("john Kelly", 105))
