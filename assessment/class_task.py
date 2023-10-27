def list_of_numbers(my_list):
    return my_list


def odd_numbers(my_list):
    return list(range(1, 21, 2))


def odd_number_check(list1):
    return list1 % 2 == 1


def odd_number_check(my_list):
    return [number for number in my_list if number % 2 != 0]


def doubling_number_in_list(my_list):
    return [i * 2 for i in my_list if i % 2 == 1]


def doubling_number_in_list2(my_list):
    answer = []
    for number in my_list:
        if number % 2 == 1:
            answer.append(number * 2)
            return answer


def exercise4(my_list):
    result = [i * 2 for i in my_list if i % 2 == 1]
    result[4:8] = [0] * len(my_list[4:8])
    return result


def exercise5(list1, list2):
    return [x + y for x, y in zip(list1, list2)]
