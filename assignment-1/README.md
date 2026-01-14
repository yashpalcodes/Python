Python Basics: Arithmetic and String Formatting
                
This repository contains two introductory Python scripts designed
to demonstrate user input handling, basic mathematical operations, 
and string formatting.

Task Overview
Task 1: Basic Calculator
        
        A script that accepts two integers from the user and 
        performs the four fundamental arithmetic operations.

        Addition: a + b
        Subtraction: a - b
        Multiplication: a * b
        Division: a / b (returns a float)


Task 2: Personalised Greeting

        A script that captures the user's 
        first and last name and returns a formatted greeting 
        using Python f-strings.
        
        How to RunEnsure Python is installed: 
        You can check by running python --version in your terminal.
        Clone or Copy the Code: Save the snippets below into .py files (e.g., calculator.py and greeting.py).Execute: Run the scripts using:Bashpython calculator.py


Code Implementation
Task 1: Arithmetic OperationsPython

# Taking integer input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Displaying results
print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)


Task 2: String FormattingPython

# Taking string input from the user
first = input("Enter your first name: ")
last = input("Enter your last name: ")

# Using f-strings for clean output
print(f"Hello, {first} {last}! Welcome to the Python program.")

Features Covered
input() function: Capturing user data.
Type Casting: Converting string input to int().
Arithmetic Operators: +, -, *, /.
F-Strings: Modern and readable string interpolation.