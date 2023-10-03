user_input = int(input('Enter a number: '))
pi = 4
second_number = 4
count = 1
while count < user_input:
    pi = pi / count
    print(pi)
    count += 2
    pi = pi - second_number / count
    print(pi)
    pi= pi + second_number/5
    print(pi)
