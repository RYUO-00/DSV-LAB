# Experiment 2d: Comparing specified parameters using a stacked area chart
# (smartphone sales units)

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---- Load dataset ----
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
