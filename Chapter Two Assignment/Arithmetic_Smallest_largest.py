number1 = int(input('Enter first number: '))
number2 = int(input('Enter Second Number: '))
number3 = int(input('Enter Third number: '))

Sum = number3 + number2 + number1
print('sum is :', Sum)
average = Sum / 3
print(f'Average is : {average} ')
product = number3 * number2 * number1
if number3 > number2 and number3 > number1:
    print(number3, ': is highest')
elif number2 > number1 and number2 > number3:
    print(number2, ': is Highest')
elif number1 > number2 and number1 > number3:
    print(number1, ': is the highest')

if number3 < number2 and number3 < number1:
    print(number3, ': is lowest')
elif number2 < number1 and number2 < number3:
    print(number2, ': is lowest')
elif number1 < number2 and number1 < number3:
    print(number1, ': is the lowest')



