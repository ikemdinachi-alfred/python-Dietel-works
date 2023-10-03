user_input = int(input('Enter number: '))
first_Number = user_input / 100
n = user_input % 100
second_nuber = n / 10
third_number = n % 10
binary_one = first_Number ** 100
binary_two = second_nuber ** 10
binary_three = third_number ** 1

print(f'The binary conversion of {user_input} is {binary_one:.1f}{binary_two:.1f} {binary_three:.1f}')
