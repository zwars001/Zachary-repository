print('Assignment 3')
print()
program = 'This program simply tests the basics of indexing and string/text combinations using python'
print('Programing Language:', program[84:])
print()
month = input('Enter birth month:')
day = int(input('Enter birth day:'))
year_birth = int(input('Enter birth year:'))
year_current = int(input('Enter current year:'))
age = (year_current - year_birth)
print()
print('I am currently', age, 'years old, and my birthday is', month, day, year_birth)
statement = 'I am currently years old, and my birthday is'
print(statement[:14], age, statement[15:], month, day, year_birth)
