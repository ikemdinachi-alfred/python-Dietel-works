

number = 0
fibonacci = 1
result = number + fibonacci
while number < 50:
    print(number, end= '    ')
    number = fibonacci
    fibonacci = result
    result = number + fibonacci

