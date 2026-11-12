
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('C:\\Users\\ADMIN\\Desktop\\dsv_programs\\anage_data.csv') if os.path.exists('C:\\Users\\ADMIN\\Desktop\\dsv_programs\\anage_data.csv') else pd.DataFrame({
    'Class': ['Aves', 'Aves', 'Mammalia', 'Mammalia', 'Reptilia', 'Reptilia'],
    'Body mass (g)': [100, 200, 5000, 10000, 300, 400],
    'Maximum longevity (yrs)': [5, 10, 15, 20, 8, 12]
})


data = data.dropna(subset=['Maximum longevity (yrs)', 'Body mass (g)'])
birds = data[ (data['Class'] == 'Aves') & (data['Body mass (g)'] < 20000) ]
mass = birds['Body mass (g)']
longevity = birds['Maximum longevity (yrs)']


fig = plt.figure(figsize=(8, 8), dpi=150, constrained_layout=True)
grid = fig.add_gridspec(4, 4)
top = fig.add_subplot(grid[0, :-1])
right = fig.add_subplot(grid[1:, -1])
main = fig.add_subplot(grid[1:, :-1])

main.scatter(mass, longevity)
top.hist(mass, bins=80, density=True)
right.hist(longevity, bins=80, density=True, orientation='horizontal')
top.set_xticks([])
right.set_yticks([])

main.set_xlabel('Body mass in grams')
main.set_ylabel('Maximum longevity in years')
fig.suptitle('Scatter plot with marginal histograms')
plt.show()
