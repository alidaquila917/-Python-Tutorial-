import math

# Take input for radius
radius = float(input("Enter the radius of the circle: "))

# Calculate circumference
circumference = 2 * math.pi * radius

# Calculate area
area = math.pi * (radius ** 2)

# Print the calculated values
print("Circumference:", circumference)
print("Area:", area)
