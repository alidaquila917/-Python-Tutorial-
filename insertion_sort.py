import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate a random list of numbers
random_list = [random.randint(1, 100) for _ in range(10)]
print("Original list:", random_list)

# Apply insertion sort algorithm
insertion_sort(random_list)

# Print the sorted list
print("Sorted list:", random_list)
