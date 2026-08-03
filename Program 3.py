import math

# Accept a floating-point number from the user
num = float(input("Enter a floating-point number: "))

# Display results
print("Square:", num ** 2)
print("Cube:", num ** 3)

if num >= 0:
    print("Square Root:", math.sqrt(num))
else:
    print("Square Root: Not possible for negative numbers")

print("Ceiling Value:", math.ceil(num))
print("Floor Value:", math.floor(num))
print("Absolute Value:", abs(num))
print("Type of Variable:", type(num))
print("Memory Address (ID):", id(num))
