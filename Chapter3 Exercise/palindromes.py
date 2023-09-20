
number = int(input(" Enter five Digit integer: "))

i = number//10000
b = number // 1000 % 10
d = number // 100 % 10
c = number // 10 % 10
f = number % 10
result = i, b, d, c, f
result2 = f, c, d, b, i

if result == result2:
    print(i, b, d, c, f, ':  is a palindrome')
elif result != result2:
    print(i, b, d, c, f, ':  is not a palindrome')

