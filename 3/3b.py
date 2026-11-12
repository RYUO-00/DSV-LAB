# Experiment 3b: Scatter plot with marginal histograms
# Needs 'ange-data.csv' (AnAge dataset) in the same folder.
# If the file is missing, small dummy data is generated so the program still runs.
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Load data ----------
if os.path.exists('ange-data.csv'):
    data = pd.read_csv('ange-data.csv')
else:
    print("ange-data.csv not found, using dummy data")
    rng = np.random.default_rng(0)
    n = 200
    mass_dummy = np.exp(rng.normal(4, 1.5, n))                  # body mass in grams
    long_dummy = 5 + 0.5 * np.log(mass_dummy) + rng.normal(0, 3, n)
    data = pd.DataFrame({'Class': 'Aves',
                         'Maximum longevity (yrs)': long_dummy,
                         'Body mass (g)': mass_dummy})

# ---------- Preprocessing ----------
longevity = 'Maximum longevity (yrs)'
mass = 'Body mass (g)'

# keep only rows where both values are valid numbers
data = data[np.isfinite(data[longevity]) & np.isfinite(data[mass])]

# keep only birds (Aves) with mass below 20000 g
aves = data[data['Class'] == 'Aves']
aves = aves[aves[mass] < 20000]

# ---------- Create figure and grid ----------
fig = plt.figure(figsize=(8, 8), dpi=150, constrained_layout=True)
gs = fig.add_gridspec(4, 4)

# ---------- Specify subplots ----------
histx_ax = fig.add_subplot(gs[0, :-1])      # top histogram
histy_ax = fig.add_subplot(gs[1:, -1])      # right histogram
scatter_ax = fig.add_subplot(gs[1:, :-1])   # main scatter plot

# ---------- Create plots ----------
scatter_ax.scatter(aves[mass], aves[longevity])
histx_ax.hist(aves[mass], bins=80, density=True)
histy_ax.hist(aves[longevity], bins=80, density=True, orientation='horizontal')

# hide the tick labels of the marginal histograms
histx_ax.set_xticks([])
histy_ax.set_yticks([])

# ---------- Add labels ----------
scatter_ax.set_xlabel('Body mass in grams')
scatter_ax.set_ylabel('Maximum longevity in years')
fig.suptitle('Scatter plot with marginal histograms')
plt.show()
