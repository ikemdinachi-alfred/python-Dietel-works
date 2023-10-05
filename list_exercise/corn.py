number = [15, 20, 25, 20, 10, 5]
total = 0
multiply = 1
largest = 0
smallest = 25
for count in number:
    total = total + count
    multiply = multiply * count
    if count > largest: largest = count
    if count < smallest: smallest = count

print(f'The sum is {total}')
print(f'The product is {multiply}')
print(f'The largest is {largest}')
print(f'The smallest is {smallest}')
