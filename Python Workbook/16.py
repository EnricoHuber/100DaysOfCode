"""
Write a program that begins by reading a radius, r , from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r . Use the pi constant in the math module in your
calculations.
"""

from math import pi


def area(r):
    return pi * pow(r, 2)


def volume(r):
    return (4 * pi * pow(r, 3)) / 3


radius = float(input("Insert the radius: "))
print(f"Area is {area(radius):.2f}\n"
      f"Volume is {volume(radius):.2f}")
