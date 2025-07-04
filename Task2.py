import math
n=int(input("Enter a number: "))
if n>=0:
    print("Square root of the number",n,"is:",math.sqrt(n))
else:
    print("Square root of the number",n,"is not possible.")
if n>0:
    print("Natural logarithm (log base e) of the number",n,"is:",math.log(n, math.e))
else:
    print("Natural logarithm (log base e) of the number",n,"is not possible.")

print("Sine of the number (in radians)",n,"is:",math.sin(n))
