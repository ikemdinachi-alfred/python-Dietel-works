
total=0
count=0
student_score = int(input("Enter Student Score or press -1 to stop: "))
while student_score !=-1:
    student_score = int(input("Enter Student Score or press-1 to stop: "))
    total=total+student_score
    count += 1
average=total/10
print("total score ",total , "Student Average score is:  ", average)

