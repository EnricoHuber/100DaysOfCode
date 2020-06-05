"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
"""

length = int(input("Insert the field's length: "))
width = int(input("Insert the field's width: "))
area = length * width
area_in_acres = area * 43.56
print(area_in_acres)