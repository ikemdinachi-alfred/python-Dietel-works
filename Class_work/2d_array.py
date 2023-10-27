catName = []
while True:
    print("Enter name of cat " + str(len(catName) + 1) + ' or press z to stop:  ')
    cat = input()
    if cat == 'z': break
    catName = catName + [cat]
print("The cat name are: ")
for i in catName:
    print(' ' + catName)
