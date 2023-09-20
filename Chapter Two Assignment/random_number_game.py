import random

guessed = random.randint(1, 5)
guess = int(input('Enter a number between 1-5: '))
while guessed != guess:
    guess = int(input('Enter a number between 1-5: '))
print(guessed, " Match with ", guess)
print("you win")