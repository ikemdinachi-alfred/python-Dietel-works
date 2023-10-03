def average_score(score):
    return sum(score) / len(score)


exam_scores = []
for i in range(10):
    scores = int(input("Enter number: "))
    exam_scores.append(scores)

print(average_score(exam_scores))
