import numpy as np

# Creating a 1-dimensional NumPy array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1-D Array:")
print(arr_1d)
print("Shape:", arr_1d.shape)  # Shape of the array
print("Dimension:", arr_1d.ndim)  # Number of dimensions

# Creating a 2-dimensional NumPy array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)
print("Dimension:", arr_2d.ndim)

# Performing operations on NumPy arrays
# Element-wise addition, subtraction, multiplication, and division
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("\nElement-wise Addition:")
print(arr1 + arr2)

print("Element-wise Subtraction:")
print(arr1 - arr2)

print("Element-wise Multiplication:")
print(arr1 * arr2)

print("Element-wise Division:")
print(arr1 / arr2)

# NumPy functions
print("\nMean of arr1:", np.mean(arr1))  # Mean
print("Maximum value in arr2:", np.max(arr2))  # Maximum value
print("Minimum value in arr2:", np.min(arr2))  # Minimum value
