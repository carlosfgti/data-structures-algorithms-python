num1 = 11
num2 = num1

print("Before num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("num1 points to: ", id(num1))
print("num2 points to: ", id(num2))

print("\nAfter num2 value is updated:")
num2 = 3
print("num1 = ", num1)
print("num2 = ", num2)
print("num1 points to: ", id(num1))
print("num2 points to: ", id(num2))