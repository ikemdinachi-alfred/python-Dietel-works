students = {
    "dike": 33,
    "ope": 25,
    "melody": 20,
    "precious": 27,
}


def student_age():
    name = str(input(" Enter your name: ")).lower()
    for key in students.keys():
        if key == name:
            return f' Hi, {name} you are {students.get(key)} years old'
        else:
            while name not in students.keys():
                age = int(input("name not found, Enter Your age: "))
                students.update({name: age})
                return f' Hi, {name} you are {students.get(name)} years old'


# print(student_age())

list = [[2, 4, 5, 6], [2, 4, 5, 6]]


def sum_list():
    total = 0
    for x in list:
        total += x
    return total


# print(sum_list())


def count_number_of_Characters(string):
    char_counts = {}
    for char in string:
        if char in char_counts.keys():
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


input = "google.com'"
output = count_number_of_Characters(input)
print()

def count_number_of_Characters1(string):
    return {character: string.count(character) for character in string}
print(count_number_of_Characters1("value"))


#check if a  word start with p
words = "printers"

def check_if_word_start_with_a_word(word: str):
    if word.startswith("p"):
        print("p is present")
    else: print("p is absent ")

# the replace method
# to split

my_sch = "Semicolon africa technology"
res = my_sch.split("s")
print(res)

# the join method
# alphabets = ["A", "B", "c", "D"]
print("$ ".join(["A", "B", "C", "D"]))

#partition method
print(my_sch.partition("m"))
