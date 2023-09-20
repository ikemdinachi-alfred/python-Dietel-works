amount = int(input('Enter investment Amount: $'))
count = 0
while count < 30:
    Roi= amount * 0.10
    new_amount = amount + Roi
    count += 1
    amount = new_amount
    print(f' your Roi is ${Roi:.2f} your investment now in {count} years is $ {new_amount:.2f} ')



