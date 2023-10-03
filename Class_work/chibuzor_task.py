number = int(input(f"Enter student score 1: "))
total = number
count = 1
maximum = 0
average = number
minimum = number
while count < 10:
    number = int(input(f"Enter student score {count+1}: "))
    total = total + number
    average = total / count
    count += 1
    if number > maximum: maximum = number
    if number < minimum: minimum = number
print(f'The total is : {total}')
print(f' The average is: {average}')
print(f'The maximum is: {maximum}')
print(f'The minimum is: {minimum}')
