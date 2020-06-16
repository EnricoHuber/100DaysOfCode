"""
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
due to gravity is 9.8m/s^2. You can use the formula to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
"""


def v_f(h, g, v_i):
    return (pow(v_i, 2) + (2 * g * h))**(1/2)


height = float(input("Insert the height: "))
g = 9.8
v_i = 0
print(f"Final speed is {v_f(height, g, v_i)}")
