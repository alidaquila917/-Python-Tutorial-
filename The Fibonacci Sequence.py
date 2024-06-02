# Define required variables
n = int(input("Enter the number of Fibonacci numbers you want: "))
fibonacci_series = []

# Start the loop to get the Fibonacci numbers
for i in range(n):
    if i == 0:
        fibonacci_series.append(0)
    elif i == 1:
        fibonacci_series.append(1)
    else:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    print(fibonacci_series[-1])