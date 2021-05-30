# a more normal tip inputter #
x = input('How much was the meal? ')

tax = 0.09
tip1 = 0.15
tip2 = 0.18
tip3 = 0.20
cost_of_meal = float(x)
total_meal_with_tax = cost_of_meal + (cost_of_meal*tax)
total_cost_15 = total_meal_with_tax + (cost_of_meal*tip1)
total_cost_18 = total_meal_with_tax + (cost_of_meal*tip2)
total_cost_20 = total_meal_with_tax + (cost_of_meal*tip3)

print('These are the tip options from 15-20 percent: $%.2f: $%.2f: $%.2f' % (total_cost_15, total_cost_18, total_cost_20))
