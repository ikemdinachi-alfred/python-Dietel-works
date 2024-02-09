def return_number(my_list: list):
    lenths = len(my_list)
    total: list = []
    for index in range(lenths):
        total.append(my_list[index])
    return total


def return_inverse_number(my_list: list):
    lenths = len(my_list)
    element = lenths
    total: list = []
    for index in range(lenths):
        total.append(my_list[element])
        element = element-1
    return (element, total)


my_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 45, 89, 90, 78]
print(return_number(my_elements))
