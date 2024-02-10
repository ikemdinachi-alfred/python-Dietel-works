def character_counter(input_values):
    char_count = {}
    for char in input_values:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


value = "semicolon.africa"
product = character_counter(value)
print(product)
