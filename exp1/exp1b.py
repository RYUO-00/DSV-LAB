# Experiment 1b: Statistical measures and basic operations using Pandas

import pandas as pd

# Example dataset (a Pandas Series with 9 values)
data = pd.Series([3, 2, 32, 76, 33, 78, 12, 34, 86])

# ---- Statistical measures ----
print("Mean:", data.mean())
print("Median:", data.median())
print("Variance:", data.var())
print("Standard Deviation:", data.std())

# ---- Indexing ----
print("Element at index 2:", data[2])

# ---- Slicing ----
print("Sliced data (from index 2 to 6):", data[2:6])

# ---- Iterating ----
print("Iterating over elements:")
for i in data:
    print(i)

# ---- Filtering ----
filt_data = data[data > 25]
print("Filtered data (elements >25):", filt_data)

# ---- Sorting ----
sort_data = data.sort_values()
print("Sorted Data:", sort_data)

# ---- Reshaping ----
# Put the Series in a DataFrame, then reshape its values into 3x3
df = pd.DataFrame({'values': data})
print("Reshaped Data (3x3):\n", df.values.reshape(3, 3))
