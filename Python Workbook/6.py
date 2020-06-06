"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
"""

meal_cost = int(input("Insert the cost of meal: "))
tip = (18 * meal_cost / 100)
tax = 15/100
total_cost = meal_cost + (meal_cost * tax) + tip
print(f"Tax: {meal_cost * tax}, tip: {tip}, total cost: {total_cost}")
