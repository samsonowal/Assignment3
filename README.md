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

Program Functionality Overview

                                 import math
                                 n = float(input("Enter a number: "))

The program starts by importing the math module, which provides access to various mathematical functions.

It then prompts the user to enter a number.

The input is converted to a float, which means the user can enter decimal values as well as integers.

Operations Performed
a. Square Root Calculation

                                 if n >= 0:
                                     print("Square root of the number", n, "is:", math.sqrt(n))
                                 else:
                                     print("Square root of the number", n, "is not possible.")

 If n is zero or positive, it calculates the square root using math.sqrt(n) and displays the result.

 If n is negative, it prints a message saying the square root is not possible, because square root of a negative number is not defined in the real number system (requires complex numbers).

b. Natural Logarithm (log base e)

                                    if n > 0:
                                           print("Natural logarithm (log base e) of the number", n, "is:", math.log(n, math.e))
                                    else:
                                           print("Natural logarithm (log base e) of the number", n, "is not possible.")

   If n is positive, it computes the natural logarithm (log base e) using math.log(n, math.e).

   If n is zero or negative, it informs the user that the logarithm is not possible because log(x) is undefined for x ≤ 0 in real numbers.

c. Sine Calculation (in Radians)

                                       print("Sine of the number (in radians)", n, "is:", math.sin(n))

   This line calculates the sine of the number assuming it is in radians using math.sin(n).

   This operation is valid for any real number, including negative numbers and zero.
   
5.   .   Output:
   
6.      ![Screenshot 2025-07-04 105636](https://github.com/user-attachments/assets/55680550-b8b5-4fcb-8bd4-fa0bddc8cb14)


7.      ![Screenshot 2025-07-04 105711](https://github.com/user-attachments/assets/66752e3e-5d37-4e57-8305-0144ddd74898)




    
