# Experiment 3d: Scatter plots to visualize correlation between groups
import matplotlib.pyplot as plt

# ---------- Data (all groups must have the same length) ----------
group_a = [118, 103, 125, 107, 111, 96, 104, 97, 96, 114,
           95, 75, 117, 98, 89, 125, 111, 100, 96, 95]
group_b = [100, 98, 61, 62, 125, 111, 100, 96, 95, 99,
           92, 91, 96, 75, 114, 98, 89, 87, 125, 111]
group_c = [100, 98, 61, 69, 70, 81, 83, 86, 96, 87,
           80, 89, 125, 111, 100, 96, 95, 94, 93, 89]
group_d = [126, 122, 86, 88, 92, 70, 84, 81, 89, 100,
           140, 131, 120, 61, 62, 63, 64, 66, 76, 86]

# ---------- 2x2 grid of scatter plots ----------
plt.figure(figsize=(12, 8), dpi=150)

plt.subplot(2, 2, 1)
plt.scatter(group_a, group_b, color='blue')
plt.xlabel('Group A')
plt.ylabel('Group B')
plt.title('Group A vs Group B')

plt.subplot(2, 2, 2)
plt.scatter(group_a, group_c, color='green')
plt.xlabel('Group A')
plt.ylabel('Group C')
plt.title('Group A vs Group C')

plt.subplot(2, 2, 3)
plt.scatter(group_a, group_d, color='red')
plt.xlabel('Group A')
plt.ylabel('Group D')
plt.title('Group A vs Group D')

plt.subplot(2, 2, 4)
plt.scatter(group_b, group_c, color='purple')
plt.xlabel('Group B')
plt.ylabel('Group C')
plt.title('Group B vs Group C')

plt.tight_layout()
plt.show()
