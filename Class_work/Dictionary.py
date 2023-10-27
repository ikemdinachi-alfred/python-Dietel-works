dictionary = {
    "II": [2, "one"],
    "I": 1,
    "V": 5,
    "III": 3,
    "X": 10,
    "XX": 20,
    "XV": 5
}
# TO know the length of the dictionary we use the len function, However,  the length of the above dictionary is
print(len(dictionary))
print(dictionary["II"])

# dictionary comprehension

list_comprehension = {n: n ** 2 for n in range(1, 11)}
print(list_comprehension)
