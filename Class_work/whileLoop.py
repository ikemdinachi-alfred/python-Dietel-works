
def multiple_print():
    for count in range(1, 51):
     if count % 5 == 0 and count % 3 == 0:
        print("fizzBuzz")
     elif count % 3 == 0:
        print("fizz")
     elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)

fizzbuzz_count = multiple_print()

print(fizzbuzz_count)