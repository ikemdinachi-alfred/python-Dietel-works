card_number = input(" Enter your card Number: ")
str(card_number)
card_check = []
total = 0
index = 0

while index < len(card_number):
    total = index
    card_check = total
    index += 1

for index in range(1, len(card_number), 2):
    card_number = index
    print(card_number, end= ' ')
