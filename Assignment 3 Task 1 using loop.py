n=5
print ("Enter a number:", n)
def factorial(n):
    if n<2:
        print("undefined")
    c = 1
    for i in range(1, n+1):
        c *= i
    return c
print("Factorial of 5 is:", factorial(n))