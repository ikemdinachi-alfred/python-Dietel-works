number = int(input('Enter investment Amount: $'))
ten_years_return = number * (1 + 0.07) ** 10
twentieth_year_return = number * (1 + 0.07) ** 20
thirtieth_year_return = number * (1 + 0.07) ** 30

one = round(ten_years_return, 2)
two = round(twentieth_year_return, 2)
three = round(thirtieth_year_return, 2)
print('your return amount After 10 years is: $', one)
print('your return amount After 20 years is: $', two)
print('your return amount After 30 years is: $', three)