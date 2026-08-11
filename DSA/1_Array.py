"""
This file demonstrates the implementation and differences between 
Python's built-in `array` module and `numpy` arrays.

Key Differences:
1. Module: `array` is built-in; `numpy` requires installation (pip install numpy).
2. Functionality: `array` is basic (1D only, standard operations); `numpy` is advance (multi-dimensional, advanced math).
3. Performance: `numpy` is highly optimized in C for bulk operations (vectorization); `array` requires traditional loops.
4. Use case: Use `array` for simple memory-efficient sequences; use `numpy` for data science, matrices, and heavy math.
"""

# =====================================================================
# 1. Using Python's built-in `array` module
# =====================================================================
import array

print("--- BUILT-IN ARRAY MODULE ---")

# Creating an array
# The first argument is the "type code". 'i' stands for signed integer.
# Other common codes: 'd' (double/float), 'u' (Unicode character).
# All elements MUST match this type.
my_array = array.array('i', [10, 20, 30, 40, 50])
print(f"Original array: {my_array}")

# Accessing elements (O(1) time complexity)
print(f"Element at index 2: {my_array[2]}")

# Insertion (O(n) time complexity - elements must shift right)
my_array.insert(2, 25) 
print(f"After inserting 25 at index 2: {my_array}")

# Appending (O(1) amortized time complexity)
my_array.append(60)
print(f"After appending 60: {my_array}")

# Deletion (O(n) time complexity - elements must shift left)
my_array.remove(25) # Removes the first occurrence of 25
print(f"After removing 25: {my_array}")

# Iteration
print("Iterating through array:")
for element in my_array:
    print(element, end=" ")
print("\n")


# =====================================================================
# 2. Using the `numpy` library
# =====================================================================
import numpy as np

print("--- NUMPY ARRAYS ---")

# Creating a 1D numpy array
# Numpy infers the data type, but you can strictly define it (e.g., dtype='int32')
np_array = np.array([10, 20, 30, 40, 50], dtype='int32')
print(f"Original NumPy array: {np_array}")
print(f"Data type: {np_array.dtype}")

# Accessing elements (O(1) time complexity)
print(f"Element at index 2: {np_array[2]}")

# Vectorized Operations (Massive performance boost)
# Notice how we don't need a loop to multiply every element by 2
np_array_doubled = np_array * 2 
print(f"Vectorized multiplication (x2): {np_array_doubled}")

# Multi-dimensional Arrays (Matrices)
# The built-in `array` module cannot do this efficiently.
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("2D NumPy Array (Matrix):")
print(matrix)

# Accessing elements in a 2D array: matrix[row, col]
print(f"Element at row 1, col 2: {matrix[1, 2]}")

# Note on Insertion/Deletion in Numpy:
# NumPy arrays are strictly fixed in size. Appending or inserting 
# actually creates a brand-new array under the hood (O(n) operation).
np_appended = np.append(np_array, [60, 70])
print(f"After appending (creates new array): {np_appended}")