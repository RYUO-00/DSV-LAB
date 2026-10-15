# Experiment 1a: Statistical measures and basic operations using NumPy

import numpy as np

# Example dataset
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# ---- Statistical measures ----
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))

# ---- Indexing ----
print("Element at index 3:", data[3])

# ---- Slicing ----
print("Sliced data from index 4 to 6:", data[4:6])

# ---- Iterating ----
print("Iterating over elements:")
for i in data:
    print(i)

# ---- Filtering ----
filt_data = data[data > 5]
print("Filtered data (elements >5):", filt_data)

# ---- Sorting ----
sort_data = np.sort(data)
print("Sorted Data:", sort_data)

# ---- Splitting ----
print("Split Data:", np.array_split(data, 2))

# ---- Combining ----
data2 = np.array([11, 12, 13])
combined = np.concatenate((data, data2))
print("Combined Data:", combined)

# ---- Reshaping ----
print("Reshaped Data (2x5):\n", data.reshape(2, 5))
