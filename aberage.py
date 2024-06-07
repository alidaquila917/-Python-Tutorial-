def calculate_average(numbers):
    # Get the sum of the numbers
    total = sum(numbers)
    # Divide the sum by the length of the list
    average = total / len(numbers)
    return average

# Example usage
number_list = [1, 2, 3, 4, 5]
print("Average:", calculate_average(number_list))
