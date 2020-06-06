"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n.
"""

number = int(input("Insert the number: "))
sum = (number * (number + 1)) // 2
print(sum)