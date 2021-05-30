# Input more options for tip and tax and output total cost and the tip by itself #
x = input('How much was the meal? ')
y = input('How much tax? ')
z = input('How much tip? ')
tax = int(y)/100
tip = int(z)/100
cost_of_meal = float(x)
total_meal_with_tax = cost_of_meal + (cost_of_meal*tax)
total_cost = total_meal_with_tax + (cost_of_meal*tip)
tip_input = cost_of_meal*tip
print('Total cost of meal: $%.2f' % total_cost)
print('Input this into the tip line: $%.2f' %tip_input)
