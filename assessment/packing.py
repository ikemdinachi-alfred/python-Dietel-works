import random
from string import hexdigits

numbers = list(range(1, 21))
num = list(range(1, 11))



def even(n):
    return n % 2 != 0


result = list(filter(lambda n: n % 2 == 1, numbers))
result2 = list(map(lambda n: n % 2 == 1, numbers))

print(list(zip(num, numbers)))

express = list(hexdigits)
print(express)

numz = random.choice(ascii('p'))
print(numz)