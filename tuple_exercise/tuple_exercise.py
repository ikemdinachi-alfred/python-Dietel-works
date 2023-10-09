def reverse_tuple(number):
    reversed_list = []
    index = len(number) - 1
    while index >= 0:
        reversed_list.append(number[index])
        index -= 1
    return tuple(reversed_list)

def find_duplicates(input_tuple):
    seen = set()
    duplicates = set()

    for item in input_tuple:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return tuple(duplicates)

# Example usage:
my_tuple = (1, 2, 3, 2, 4, 5, 6, 6, 7, 8, 9, 9)
result = find_duplicates(my_tuple)
print(result)