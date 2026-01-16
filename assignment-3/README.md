Python Mathematical Operations: Recursion & Math Module


This project demonstrates two ways to handle mathematical 
computations in Python: using Recursion for custom logic 
and the math library for advanced calculations.


Task Overview
Task 1: Recursive Factorial
    This script calculates the factorial of a non-negative
     integer using a recursive function.
     <br>
     Logic: The function calls itself with $n-1$ until 
     it reaches the base case ($n=0$ or $n=1$).
     
     Formula: $n! = n \times (n-1) \times \dots \times 1$
     
     <br>
Task 2: The Math Module
     <br>
     This script utilizes Python's built-in math library 
     to perform more complex operations that are common 
     in engineering and data science.
     <br>
     Square Root: Calculates $\sqrt{n}$.
     <br>
     Logarithm: Calculates the natural logarithm ($\ln(n)$).
     <br>
     Sine: Calculates the sine of $n$ (where $n$ is in radians).
     
     <hr><br>
Code Implementation 
     <br>
Task 1: Factorial using RecursionPythondef factorial(n):
# Base case: 0! and 1! are both 1
if(n == 0 or n == 1):
    return 1
# Recursive step: n * (n-1)!
return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {factorial(n)}")
     <br>
Task 2: Advanced Math FunctionsPythonimport math

n = int(input("Enter a number: "))

print("Square root: ", math.sqrt(n))
print("Logarithm:  ", math.log(n))
print("Sine:       ", math.sin(n))

<br>

Concepts LearnedRecursion: 

Breaking a problem down into smaller versions of itself.

Base Case: Preventing infinite loops in recursive functions.
Module Importing: Using import math to access pre-built C-optimized functions.

Mathematical Constants: Handling floating-point results for trigonometric and logarithmic functions.
<br>
How to Run
Ensure you have Python 3.x installed.Save the code into
 a file named math_ops.py.Run the script via your terminal:
                            
                            python math_ops.py