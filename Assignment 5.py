print('This is a pressure valve system')
print()
print('You need to have three valves that need to be adjusted to get a value between 35 and 37')
print('Having a total PSI above 37 will break the system')
print()
valve1 = int(input('Enter first PSI value for valve 1:'))
valve11 = int(input('Enter second PSI value for Valve 1 :'))
valve111 = int(input('Enter third PSI value for Valve 1 :'))
valve1111 = int(input('Enter fourth PSI value for Valve 1 :'))
valve11111 = int(input('Enter fourth PSI value for Valve 1 :'))
print()
valve2 = int(input('Enter first PSI value for valve 2:'))
valve22 = int(input('Enter second PSI value for Valve 2 :'))
valve222 = int(input('Enter third PSI value for Valve 2 :'))
valve2222 = int(input('Enter fourth PSI value for Valve 2:'))
valve22222 = int(input('Enter fourth PSI value for Valve 2:'))
print()
valve3 = int(input('Enter first PSI value for valve 3:'))
valve33 = int(input('Enter second PSI value for Valve 3 :'))
valve333 = int(input('Enter third PSI value for Valve 3 :'))
valve3333 = int(input('Enter fourth PSI value for Valve 3:'))
valve33333 = int(input('Enter fourth PSI value for Valve 3:'))
sum1 = valve1+valve11+valve111+valve1111+valve11111
sum2 = valve2+valve22+valve222+valve2222+valve22222
sum3 = valve3+valve33+valve333+valve3333+valve33333
print()
print('Enter a PSI values for Valve 1 given the following options-', valve1, ',', valve11, ',', valve111, ',', valve1111, ',', valve11111)
print('Enter a PSI values for Valve 2 given the following options-', valve2, ',', valve22, ',', valve222, ',', valve2222, ',', valve22222)
print('Enter a PSI values for Valve 3 given the following options-', valve3, ',', valve33, ',', valve333, ',', valve3333, ',', valve33333)
print()
if sum1 >= 35 and sum1 <= 37:
    print('Valve 1 total PSI is within optimal range.')
    print(f'PSI for Valve 1: {sum1}')
    print()
elif sum1 >= 37:
    print('Valve 1 has overloaded the system. System is shutting down for safety requirements ')
elif sum1 < 35:
    print('Re-do the PSI inputs for Valve 1')
    print()
if sum2 >= 35 and sum2 <= 37:
    print('Valve 2 total PSI is within optimal range.')
    print(f'PSI for Valve 2: {sum2}')
    print()
elif sum2 >= 37:
    print('Valve 2 has overloaded the system. System is shutting down for safety requirements ')
elif sum2 < 35:
    print('Re-do the PSI inputs for Valve 2')
    print()
if sum3 >= 35 and sum3 <= 37:
    print('Valve 3 total PSI is within optimal range.')
    print(f'PSI for Valve 3: {sum3}')
    print()
elif sum3 >= 37:
    print('Valve 3 has overloaded the system. System is shutting down for safety requirements ')
elif sum3 < 35:
    print('Re-do the PSI inputs for Valve 3')
print()