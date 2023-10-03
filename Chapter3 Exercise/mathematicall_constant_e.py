
constant_e = int(input('Enter mathematical constant \'e\' value: '))
n = 1
count = 1
while count <= constant_e:
    n = n + 1/count
    count += 1
print(n)
