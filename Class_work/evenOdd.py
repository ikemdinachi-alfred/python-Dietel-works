even_numbers = []
for even in range (2, 51):
     if even % 2 ==0:
       even_numbers.append(even)
     Average = sum(even_numbers) / len(even_numbers)
     print(Average)