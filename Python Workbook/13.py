"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.

A one dollar coin was introduced in Canada in 1987. It is referred to as a
loonie because one side of the coin has a loon (a type of bird) on it. The two
dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is
derived from the combination of the number two and the name of the loonie.
"""

tooney = 200
looney = 100
quarter = 25
dime = 10
nickel = 5

coins = int(input("Insert the number of cents: "))

n_tooney = coins // tooney
coins = coins - (n_tooney * tooney)

n_looney = coins // looney
coins = coins - (n_looney * looney)

n_quarter = coins // quarter
coins = coins - (n_quarter * quarter)

n_dime = coins // dime
coins = coins - (n_dime * dime)

n_nickel = coins // nickel
coins = coins - (n_nickel * nickel)

print(f"Rest given with:\n{n_tooney} TOONEY\n{n_looney} LOONEY\n{n_quarter} QUARTER\n{n_dime} DIME\n{n_nickel} NICKEL")
