"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""
from math import pi



def volume(r, h):
    area = pi * pow(r, 2)
    return area * h


radius = float(input("Insert the radius: "))
height = float(input("Insert the height: "))
print(f"Volume of cilinder is {volume(radius, height):.1f}")
