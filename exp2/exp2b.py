# Experiment 2b: Creating a bar plot (movie comparison)

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---- Load dataset ----
# (If the CSV is missing, sample data is created so the program still runs)
if not os.path.exists('moviescores.csv'):
    sample = pd.DataFrame({
        'Movie Title': ['The Shape of Water', 'Black Panther', 'Dunkirk',
                        'The Martian', 'The Hobbit: An Unexpected Journey'],
        'Tomatometer': [91, 97, 92, 91, 65],
        'AudienceScore': [73, 79, 81, 91, 83],
    })
    sample.to_csv('moviescores.csv', index=False)

movie_scores = pd.read_csv('moviescores.csv')

# ---- Create figure ----
plt.figure(figsize=(10, 5), dpi=300)

# ---- Creating the bar plot (two bars per movie, side by side) ----
pos = np.arange(len(movie_scores['Movie Title']))
width = 0.3

plt.bar(pos - width / 2, movie_scores['Tomatometer'], width, label='Tomatometer')
plt.bar(pos + width / 2, movie_scores['AudienceScore'], width, label='AudienceScore')

# ---- Specifying ticks ----
plt.xticks(pos, rotation=10)
plt.yticks(np.arange(0, 101, 20))

# ---- Get current axes for setting tick labels and horizontal grid ----
ax = plt.gca()

# Set tick labels
ax.set_xticklabels(movie_scores['Movie Title'])
ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])

# ---- Minor ticks for y-axis in the interval of 5 ----
ax.set_yticks(np.arange(0, 100, 5), minor=True)

# ---- Major horizontal grid with solid lines ----
ax.yaxis.grid(which='major')

# ---- Minor horizontal grid with dashed lines ----
ax.yaxis.grid(which='minor', linestyle='--')

# ---- Title and legend ----
plt.title('Movie comparison')
plt.legend()
plt.show()
