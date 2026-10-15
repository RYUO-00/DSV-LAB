# Experiment 2d: Comparing specified parameters using a stacked area chart
# (smartphone sales units)

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---- Load dataset ----
# (If the CSV is missing, sample data is created so the program still runs)
if not os.path.exists('smartphone_sales.csv'):
    sample = pd.DataFrame({
        'Quarter': ['3Q16', '4Q16', '1Q17', '2Q17', '3Q17', '4Q17', '1Q18', '2Q18'],
        'Apple':   [45500, 77000, 51500, 44000, 45000, 73000, 52000, 44000],
        'Samsung': [72000, 77000, 79000, 83000, 87000, 74000, 79000, 74000],
        'Huawei':  [34000, 38000, 33000, 35000, 36000, 44000, 41000, 50000],
        'Xiaomi':  [15000, 18000, 15000, 22000, 27000, 29000, 28000, 33000],
        'OPPO':    [20000, 27000, 29000, 25000, 30000, 28000, 27000, 25000],
    })
    sample.to_csv('smartphone_sales.csv', index=False)

sales = pd.read_csv('smartphone_sales.csv')

# ---- Create figure ----
plt.figure(figsize=(10, 6), dpi=300)

# Legend labels = the company columns
labels = ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'OPPO']

# ---- Stacked area plot ----
plt.stackplot('Quarter', 'Apple', 'Samsung', 'Huawei', 'Xiaomi', 'OPPO',
              data=sales, labels=labels)

plt.legend()
plt.xlabel('Quarters')
plt.ylabel('Sales units in thousands')
plt.title('Smartphone sales units')
plt.show()
