def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number: "))
result = factorial(n)
result = int(result)
print("Factorial of",n, "is:",result)
