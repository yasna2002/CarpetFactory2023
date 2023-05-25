import numpy as np


def matrix_match_percentage(matrix1, matrix2):
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
