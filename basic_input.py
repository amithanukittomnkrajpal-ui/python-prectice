# Basic Input Practice
# Created by: Amit
# Purpose: Practice user input and output in Python

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name)
print("Your age is", age)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2
print("Sum of two numbers is:", total)
# Check eligibility based on age

age = int(input("Enter your age again for eligibility check: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
