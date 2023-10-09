number = [15, 20, 25, 20, 10, 1, 500]
total = 0
multiply = 1
largest = number[0]
smallest = number[0]
for count in number:
    total = total + count
    multiply = multiply * count
    if count > largest: largest = count
    if count < smallest: smallest = count

print(f'The sum is {total}')
print(f'The product is {multiply}')
print(f'The largest is {largest}')
print(f'The smallest is {smallest}')
