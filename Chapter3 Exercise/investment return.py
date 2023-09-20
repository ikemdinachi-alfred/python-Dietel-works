
number = int(input('Enter investment Amount: $'))
count = 1
while count <= 30:
    one_years_return = number * (1 + 0.07) ** count
    amount = round(one_years_return, 2)
    print('your return amount After', count,  'years is: $', amount)
    count += 1
