
user_input = int(input('Enter a number: '))
# Initialize denominator
denominator = 1

# Initialize sum
sum = 0

for count in range(6):

     # even index elements are positive
     if count % 2 == 0:
          sum += 4 / denominator
     else:

          # odd index elements are negative
          sum -= 4 / denominator

     # denominator is odd
     denominator += 2

print(sum)



