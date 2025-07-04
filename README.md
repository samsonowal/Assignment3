# Assignment3
# Python 3.13.5
Task 1: Calculate Factorial Using a Function 

Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
4.   Detailed Breakdown:
   
  a. Function Definition:

                    def factorial(n):
                         if n < 2:
                            return 1
                          else:
                            return n * factorial(n - 1)

  This defines a recursive function factorial(n).

   If n is less than 2 (i.e., n = 0 or n = 1), it returns 1, because 0! = 1! = 1 (base case).

   Otherwise, it calls itself with n-1 and multiplies the result by n. This continues until it reaches the base case.

  b. User Input:

                       n = int(input("Enter a number: "))


  Prompts the user to enter a number.

  Converts the input from a string to an integer and stores it in the variable n.

  c. Factorial Calculation and Output:

                       result = factorial(n)
                       result = int(result)
                       print("Factorial of", n, "is:", result)
 
  Calls the factorial function with the user-provided n and stores the result in result.

   Converts the result to an integer (though this step is unnecessary because the result is already an integer).

   Prints the factorial value.
    
5.   Output:
6.   
     ![Screenshot 2025-07-04 100530](https://github.com/user-attachments/assets/3077a9b8-2e02-488b-ad8a-ebb35e5f9b32)



Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
  o   Square root of the number
  o   Natural logarithm (log base e) of the number
  o   Sine of the number (in radians)
3.   Displays the calculated results.
4.   Detailed Breakdown:

 a. Import the math Module

                      import math

   Imports Python’s built-in math module, which provides advanced mathematical functions like square root, logarithm, trigonometric functions, etc.

 b. User Input

                      n = int(input("Enter a number: "))

  Prompts the user to enter a number.

  Converts the input from a string to an integer and stores it in variable n.

 c. Square Root Calculation

                        print("Square root of the number", n, "is:", math.sqrt(n))

   Uses math.sqrt(n) to calculate the square root of n.

   For example, if n = 9, it outputs 3.0.

 d. Natural Logarithm (Base e)

                        print("Natural logarithm (log base e) of the number", n, "is:", math.log(n, math.e))

  Calculates the natural logarithm of n using math.log(n, math.e).

  You could also simply write math.log(n) because the default base is e.

 e. Sine of the Number (in Radians)

                        print("Sine of the number (in radians)", n, "is:", math.sin(n))

   Calculates the sine of n using math.sin(n), treating n as a value in radians.
    
5.   .   Output:
6.   ![Screenshot 2025-07-04 102959](https://github.com/user-attachments/assets/822727d3-1262-4c03-9b0e-c17fbb9a6f4a)

    
