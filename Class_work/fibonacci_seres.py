
def fibonacci(fibonacci_Number):
 number = 0
 count = 1
 result = number + count
 while number < fibonacci_Number:
    print(number, end= '  ')
    number = count
    count = result
    result = number + count

result = fibonacci(50)

print(result)