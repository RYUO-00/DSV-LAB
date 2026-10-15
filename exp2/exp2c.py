# Experiment 2c: Stacked bar plot to visualize a specified parameter
# (daily total sales, split by smoker / non-smoker)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---- Load the built-in 'tips' dataset ----
bills = sns.load_dataset('tips')

days = ['Thur', 'Fri', 'Sat', 'Sun']
days_range = np.arange(len(days))
smoker = ['Yes', 'No']

# Bills for each day
bills_by_days = [bills[bills['day'] == day] for day in days]

# Bills for each day, split by smoker (Yes / No)
bills_by_days_smoker = [[bills_by_day[bills_by_day['smoker'] == s] for s in smoker]
                        for bills_by_day in bills_by_days]

# Total bill amount for each (day, smoker) pair
total_by_days_smoker = [[bills_by_days_smoker[day][s]['total_bill'].sum()
                         for s in range(len(smoker))]
                        for day in days_range]

totals = np.asarray(total_by_days_smoker)

# ---- Create figure ----
plt.figure(figsize=(10, 5), dpi=300)

# Smoker bars at the bottom, non-smoker bars stacked on top
plt.bar(days_range, totals[:, 0], label='Smoker')
plt.bar(days_range, totals[:, 1], bottom=totals[:, 0], label='Non-Smoker')

plt.legend()
plt.xticks(days_range)

ax = plt.gca()
ax.set_xticklabels(days)
ax.yaxis.grid()

plt.ylabel('Daily total sales in $')
plt.title('Restaurant performance')
plt.show()
