
user_input = int(input('Enter a number: '))
denominator = 1

sum = 0

for count in range(6):

     if count % 2 == 0:
          sum += 4 / denominator
     else:

          sum -= 4 / denominator
     denominator += 2

print(sum)



