import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate a random list of numbers
random_list = [random.randint(1, 100) for _ in range(10)]
print("Original list:", random_list)

# Apply bubble sort algorithm
bubble_sort(random_list)

# Print the sorted list
print("Sorted list:", random_list)