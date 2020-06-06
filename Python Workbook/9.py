"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
"""

money_depos = int(input("Insert the money deposited: "))
interest = 4/100
money_available = money_depos
for year in range(1, 4):
    money_available = money_available + (interest * money_available)
    print(f"Money available after {year} years: {money_available:.2f}")
