"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by T degrees Celsius can be
computed using the formula: q = mCT.

Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.

Extend your program so that it also computes the cost of heating the water. Electricity
is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.
"""

def energy(m, t):
    global specific_heat
    return m * specific_heat * t


water_mass = float(input("Insert the mass of water: "))
temperature_variation = float(input("Insert the temperature change: "))
specific_heat = 4.186

print(f"Energy is {energy(water_mass, temperature_variation)} J")
joule_to_kwh = 2.77778e-7
print(f"Cost of heating the water is {(energy(water_mass, temperature_variation) * joule_to_kwh) * 0.089:.5f} $")


