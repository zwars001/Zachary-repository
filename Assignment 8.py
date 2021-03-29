import random
print('This is a breakeven simulator to calculate whether you would attain a profit or a loss')
print()
product = input('What product would you like to sell?:')
sell_price = float(input(f'What is the selling price for one unit of {product}?:'))
unit_cost = float(input(f'What is the cost for one unit of {product}?:'))
fixed_cost = float(input(f'What is the total fixed cost for associated with {product}?:'))
max_demand = int(input(f'What is the expected maximum number of units of {product}you expect to sell?:'))
min_demand = int(input(f'What is the expected minimum of units of {product}you expect to sell?:'))
print()
simulation = int(input('Please enter the number of times you would like the program to run the simulation:'))
print()
for i in range(1, simulation+1):
    ran = random.randint(min_demand, max_demand)
    break_even = float(round(((sell_price * ran) - (unit_cost * ran) - fixed_cost), 2))
    print(f'Break Even {i}: ${break_even}')
print()
profitability = (break_even/simulation)*100
print(f'The chance of profitabilty is:${profitability}')