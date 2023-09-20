
#write a python program that prints all the numbers
#from 0 to 6 except 3 and 6;
pass
count=0
while count<6:
    number=count
    count+=1
    if number == 3 or number == 6:
        continue
    print(number, end=' ')

#
for number in range(7):
    if number==3 or number==6:
        continue
    print(number, end=" " )