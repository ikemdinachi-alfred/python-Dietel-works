
first_number = float(input("Enter  first Number: "))
second_number = float(input("Enter Second Number: "))
third_number = float(input("Enter Third Number: "))
if first_number < second_number:
    if second_number < third_number:
        print (first_number, "<", second_number, "<", third_number)
    else:
        if first_number < third_number:
            print (first_number, "<", third_number, "<", second_number)
        else:
            print (third_number, "<", first_number, "<", second_number)
else:
    if third_number < second_number:
        print (third_number, "<", second_number, "<", first_number)
    else:
        if third_number < first_number:
            print (second_number, "<", third_number, "<", first_number)
        else:
            print (second_number, "<", first_number, "<", third_number)
            