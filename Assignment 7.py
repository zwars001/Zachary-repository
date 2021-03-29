print('This is a shopping cart app.')
print()
item = []
cost = []
loopspend = float(input('How much money do you have to spend?:'))
while loopspend > 0:
    loopitem = input('Enter the item name:')
    item.append(loopitem)
    loopcost = int(input('Cost of item:'))
    cost.append(loopcost)
    loopspend = (loopspend-loopcost)
    print()
    print(f'Remaining money:${round(loopspend,2)}')
print()
if loopspend < 0:
    print('You have made a calculation error and over spent. Please retry')
else:
    for i, j in zip(item, cost):
        print(f'Item:{i}')
        print(f'Cost:${j}')
        print()
    print(sum(cost))