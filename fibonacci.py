def fibonacci(n):
   
    if n == 0:
        return 0
    elif n == 1:
        return 1
   
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = 6
print("Fibonacci number at index", num, "is", fibonacci(num))