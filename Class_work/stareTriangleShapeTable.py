

picture = [
[1, 0, 0, 0, 0],
[1, 1, 0, 0, 0],
[1, 1, 1, 0, 0],
[1, 1, 1, 1, 0],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 0],
[1, 1, 1, 0, 0],
[1, 1, 0, 0, 0],
[1, 0, 0, 0, 0,]
]
for pixel in picture:
    for ing in pixel:
        if ing ==0:
            print("  ", end= ' ')
        else:
         print('*', end=' ')

    print()