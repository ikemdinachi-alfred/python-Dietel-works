def confirm_the_existence_of_a_number_in_a_list(lis, number):
    lis = [4, 5, 5, 6, 7]
    number = [9]
    if number is lis:
        return True
    else:
        return False


print(confirm_the_existence_of_a_number_in_a_list(lis=[4, 5, 7, 8], number=[4]))


def confirm_the_existence_of_a_vowel(vowel, letter):
    if vowel is letter:
        return True
    else:
        return False


def concatinate():
    element = [34, 45, 34, 34, 57, 98]
    element1 = [45, 78, 56, 34, 5, 6]
    new_element = element1 + element
    print(new_element)


print(concatinate())


def print_all_even_number():
    number1 = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 587, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918,
               237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
               815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]

    for index in number1:
        if index % 2 == 0:
            print(index)


print(print_all_even_number())


# def area_of_triangle():
#    base =  int(input("Enter base"))