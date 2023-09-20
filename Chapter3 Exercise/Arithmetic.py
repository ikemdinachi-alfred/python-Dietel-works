
number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
number3 = int(input('Enter third number: '))

Sum = number1 + number2 + number3
Average = Sum/4
product = number1 * number2 * number3
if number1 > number3 and number1 > number2:
    maximum = number1
elif number2 > number3 and number2 > number1:
    maximum = number2
elif number3 > number2 and number3 > number1:
    maximum = number3

if number1 < number3 and number1 < number2:
    minimum = number1
elif number2 < number3 and number2 < number1:
    minimum = number2
elif number3 < number2 and number3 < number1:
    minimum = number3


print('The sum is: ', Sum, '\n The Average is: ', Average, '\n The product is: ', product)
print('maximum is: ', maximum, "\n minimum is: ", minimum)

