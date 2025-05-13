n=5
print ("Enter a number:", n)
def factorial(n):
    if (n<2):
        return 1
    else:
        return n * (factorial(n-1))
print("Factorial of 5 is:",factorial(n))
