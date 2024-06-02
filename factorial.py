def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    
        num = int(input("Enter a number : "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        elif num == 0:
            print("Factorial of 0 is 1.")
        else:
            print("Factorial of", num, "is", factorial(num))
