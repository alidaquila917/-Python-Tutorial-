def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Please enter a positive number greater than zero.")
        elif num == 1:
            print("1 is not a prime number.")
        else:
            print("Prime numbers up to", num, "are:")
            for i in range(2, num + 1):
                if is_prime(i):
                    print(i, end=" ")
            print()
    except ValueError:
        user_input = input("Invalid input.  press Enter to try again: ")
        pass
