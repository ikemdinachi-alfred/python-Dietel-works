def sum(value: list):
    sum = 0
    for i in value:
        sum = sum + i
    return sum


def sum(value: list):
    new_lst = []
    for i in value:
        new_lst.append(i)
    return new_lst

my_list = ["fine","love","peace"]
print(sum(my_list))