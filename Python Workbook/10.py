"""
Create a program that reads two integers, a and b, from the user.Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a^b
"""
from math import log10, pow


a = int(input("Insert the first number (a): "))
b = int(input("Insert the second number (b): "))
print(f"• a+b = {a+b}")
print(f"• a-b = {a-b}")
print(f"• a*b = {a*b}")
print(f"• a*b = {a*b}")
print(f"• a/b = {a/b}")
print(f"• Remainder of a/b = {a%b}")
print(f"Log in 10-basis of a = {log10(a)}")
print(f"a^b = {pow(a, b)}")
