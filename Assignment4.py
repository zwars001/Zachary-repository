print("Welcome to Hotel 2.0")
print()

name = input('What is your name: ')

print('Memberships are as follows:\n(1) Basic - B\n(2) Advanced - A\n(3) Premium - P\n(4) VIP - V')
print('Non-members are NM.')
membership = input('Enter membership type: ')

print('Rooms can be booked as one of the following:\n(1) Single Room - S\n(2) Double Room - D\n(3) Single'
      'Queen Room - Q1\n(4) Double Queen Room - Q2\n'
      '(5) Single King Room - K1\n(6) Double King Room - K2')
room_type = input('Enter room type: ')


S = 59.99
D = 79.99
Q1 = 89.99
Q2 = 99.99
K1 = 110.99
K2 = 139.99

nights = int(input('Enter number of nights staying: '))

if room_type == 'S':
    Price = round(S * nights,2)
elif room_type == 'D':
    Price = round(D * nights, 2)
elif room_type == 'Q1':
    Price = round(Q1 * nights, 2)
elif room_type == 'Q2':
    Price = round(Q2 * nights, 2)
elif room_type == 'K1':
    Price = round(K1 * nights, 2)
elif room_type == 'K2':
    sofa = input("Do you want a sofa as well [YES/NO]: ") #allows to add the $10 if YES is chosen
    if sofa == "YES":
        Price = round((K2 + 10.00) * nights, 2) #parentheses is important to ensure the calculation is correct
    else:
        Price = round(K2 * nights, 2)
else:
    print("You have input an incorrect parameter, this program will not compute correct results") #error message in case the user had bad input


print()
print(f'Name: {name}')
print(f'Room Type: {room_type}')
print(f'Membership: {membership}')
print(f'Number of nights: {nights}')
print(f'Total Price: ${Price}')

if membership == 'B':
    Discount = round(Price * 0.9, 2)
    print(f'Membership Price: ${Discount}')
elif membership == 'A':
    Discount = round(Price * 0.85, 2)
    print(f'Membership Price: ${Discount}')
elif membership == 'P':
    Discount = round(Price * 0.75, 2)
    print(f'Membership Price: ${Discount}')
elif membership == 'V':
    Discount = round(Price * 0.6, 2)
    print(f'Membership Price: ${Discount}')
