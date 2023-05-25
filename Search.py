import numpy as np


def carpet_match_percentage(matrix1, matrix2):
    # Convert the matrices to numpy arrays for easier comparison
    arr1 = np.array(matrix1)
    arr2 = np.array(matrix2)

    # Calculate the total number of elements in the matrices
    total_elements = arr1.size

    # Count the number of matching elements
    matching_elements = np.sum(arr1 == arr2)

    # Calculate the percentage match
    percentage_match = (matching_elements / total_elements) * 100

    return percentage_match


def quicksort_high_to_low(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quicksort_high_to_low(left) + middle + quicksort_high_to_low(right)

