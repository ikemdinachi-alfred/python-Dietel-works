def divide_or_square(number):
    if number % 5 == 1:
        return number * number
    else:
        return number ** 0.50

result = divide_or_square(10)
print(result)
