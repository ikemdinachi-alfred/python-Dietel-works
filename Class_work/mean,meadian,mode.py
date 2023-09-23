
def mean_media_mode_calculatior():
 import statistics

 number_set = [10, 20, 15, 25, 5, 30, 35,  20, 10, 20]
 for count in range(0, len(number_set)):
    for counter in range(count + 1, len(number_set)):
        if number_set[count] > number_set[counter]:
            number_set[count], number_set[counter], = number_set[counter], number_set[count]


 print(number_set)
 re_arrange_list = len(number_set)
 if re_arrange_list % 2 == 0:
    m1 = number_set[re_arrange_list // 2]
    m2 = number_set[(re_arrange_list // 2) - 1]
    median = (m1 + m2) / 2
    print(f' the median is: {median}')

 mean = statistics.mean(number_set)
 print(f' the mean is: {mean}')

 mode = statistics.mode(number_set)
 print(f' the mode is: {mode}')



figure = mean_media_mode_calculatior()
print(figure)