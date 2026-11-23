# Experiment 2a: Visualizing through a line plot (stock trend)

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

google = pd.read_csv('GOOGLE_data.csv')
facebook = pd.read_csv('FB_data.csv')
apple = pd.read_csv('AAPL_data.csv')
amazon = pd.read_csv('AMZN_data.csv')
microsoft = pd.read_csv('MSFT_data.csv')

# ---- Create figure ----
plt.figure(figsize=(16, 8), dpi=300)

# ---- Plot data ----
plt.plot('date', 'close', data=google, label='Google')
plt.plot('date', 'close', data=facebook, label='Facebook')
plt.plot('date', 'close', data=apple, label='Apple')
plt.plot('date', 'close', data=amazon, label='Amazon')
plt.plot('date', 'close', data=microsoft, label='Microsoft')

# ---- Ticks ----
plt.xticks(np.arange(0, 1260, 40), rotation=70)
plt.yticks(np.arange(0, 1450, 100))

# ---- Title and y label ----
plt.title("Stock trend", fontsize=16)
plt.ylabel("Closing price in $", fontsize=14)

# ---- Grid and legend ----
plt.grid()
plt.legend()

# ---- Show plot ----
plt.show()
