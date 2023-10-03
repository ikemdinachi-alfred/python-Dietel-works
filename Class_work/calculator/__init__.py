user_input = int(input('Enter number '))
total = user_input
average = user_input
maximum = user_input
minimum = 0
for count in range(10):
    user_input = int(input('Enter number '))
    total = total + user_input
    average = total / count
    if user_input > maximum: maximum = user_input
    if user_input < minimum: minimum = user_input


print(f'The total is {total}')
print(f' The average is: {average}')
print(f'The maximum number is : {maximum}')
print(f' The minimum value is : {minimum}')
