def factorial(n):
    # Base condition
    if n == 0 or n == 1:
        return 1
    # Recursive return
    else:
        return n * factorial(n - 1)


num = 5
print("Factorial of", num, "is", factorial(num))
