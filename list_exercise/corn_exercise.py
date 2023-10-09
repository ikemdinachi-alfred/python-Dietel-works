def total(number):
    total_number = 0
    for count in number:
        total_number += count
    return total_number


def multiplication(number):
    product = 1
    for count in number:
        product *= count
    return product


def largest_number(number):
    maximum_number = number[0]
    for count in number:
        if count > maximum_number:  maximum_number = count
    return maximum_number


def smallest_number(number):
    minimum_number = number[0]
    for count in number:
        if count < minimum_number: minimum_number = count
    return minimum_number


def remove_duplicate(number):
    return set(number)
