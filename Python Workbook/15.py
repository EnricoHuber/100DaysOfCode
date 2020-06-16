"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
"""

height_in_FEET = float(input("Insert the height to be converted: "))
feet_to_inches = 12
feet_to_yards = 0.333333
feet_to_miles = 0.000189
print(f"{height_in_FEET:.6f} FEET corresponds to:\n"
      f"{height_in_FEET * feet_to_inches:.6f} INCHES\n"
      f"{height_in_FEET * feet_to_yards:.6f} YARDS\n"
      f"{height_in_FEET * feet_to_miles:.6f} MILES")

