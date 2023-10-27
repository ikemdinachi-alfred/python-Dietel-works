def sort_dictionary(sorted_dictionary):
    return dict(sorted(sorted_dictionary.items()))


tr = 0


print(sort_dictionary({1: 1, 3: 9, 5: 25, 2: 4, 4: 16}))




def addkey_value(dictionary: dict, key, value):
    dictionary.update({key: value})
    return dictionary


dictionary = {
    0: 10,
    1: 20,
}
dictionary.update({2: 50, })
print(dictionary)


