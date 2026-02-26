"""

Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division

"""
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
print("addition =",addition)
print("subtraction =", subtraction)
print("multiplication =", round(multiplication,2))
print("division =", round(division,2))
