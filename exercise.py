# Write a program that ask the user to enter the radius of a circle. The program should then calculate and print the area and perimeter of the circle.

# Define the variable.
pi = 3.142
radius = int(input())

# Calculate the area
area = pi * radius ** 2
area = round(area, 3)

# Calculate the perimeter
perimeter = 2 * pi * radius
perimeter = round(perimeter, 3) 

# Print the result of the reults 
print("\nThe area of the circle is ", area)
print("\nThe perimeter of the circle is ", perimeter)

# pi = 3.142
# radius = 10

# area = pi * radius ** 2

# perimeter = 2 * pi * radius


# print("The area of a circle is", area)
# print("The perimeter of a cricle is", perimeter)

