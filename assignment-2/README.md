Python Logic: Control Flow and Loops

This repository contains two Python tasks that 
demonstrate how to use conditional statements 
to check properties of numbers and how to use 
loops for repetitive calculations.


Task Overview

Task 1: Even or Odd Checker
        A script that determines whether a user-provided
         integer is Even or Odd using the modulo operator (%).
        Logic: A number $n$ is even if $n \pmod 2 = 0$.
        Concepts: if-else statements and arithmetic remainder.
        
        
Task 2: Summation Loop
        A script that calculates the sum of all integers from 1 up to 50
        .Logic: Iterates through a range and maintains a "running total."
        Concepts: for loops, range() function, and compound assignment (+=).
        

Code Implementation

Task 1: Conditional Logic (Even/Odd)Python
# Taking user input
n = int(input("Enter a number: "))

# Checking for divisibility by 2
if(n % 2 == 0):
    print(f"{n} is an even number.")
else:
    print(f"{n} is an odd number.")



Task 2: Iteration (Sum of 1-50)Pythonsum = 0
# Iterating from 1 to 50
for i in range(1, 51):
    sum += i

print(f"The sum of numbers from 1 to 50 is {sum}")


Key Learning Points
Modulo Operator (%): Used to find the remainder of a division.
 It is the standard way to check for parity (even vs. odd).
 
Range Function: range(1, 51) includes the starting number (1) 
but excludes the stopping number (51), effectively stopping at 50.

Accumulator Pattern: Initializing a variable (sum = 0) and 
adding to it inside a loop is a common way to aggregate data.

Usage
    Save the code into a Python file (e.g., logic_tasks.py).
    Run the script in your terminal: 
                                    Bashpython logic_tasks.py