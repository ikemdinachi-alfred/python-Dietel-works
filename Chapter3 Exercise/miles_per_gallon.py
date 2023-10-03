miles_per_gallon = 0.0
mile_driven = 0.0
average = 0.0
total = 0
count = 0

while count != -1:
    miles_per_gallon = float(input('Enter the gallons used (press -1 to end): '))
    if miles_per_gallon == -1:
        break
    mile_driven = float(input(f'Enter the miles driven: '))
    mile_driven_per_gallon_driven = mile_driven / miles_per_gallon
    print(f'The miles/ gallon for each  {mile_driven_per_gallon_driven} ')
    count += 1
    total = total + mile_driven_per_gallon_driven
    average = total / count
print(f'The overall average miles/gallon was {average}')
