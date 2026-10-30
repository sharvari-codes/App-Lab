import numpy as np

# Create a one-dimensional array from 1 to 10
arr = np.arange(1, 11)

print("Original array:", arr)

# Slicing operations
print("First 5 elements:", arr[:5])
print("Elements from index 2 to 6:", arr[2:7])
print("Alternate elements:", arr[::2])

# Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting - add 5 to every element
arr = arr + 5

print("Array after broadcasting:", arr)