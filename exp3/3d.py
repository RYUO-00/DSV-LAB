
import matplotlib.pyplot as plt

group_a = [118, 103, 125, 107, 111, 96, 104, 97, 96, 114, 95, 75, 117, 98, 89, 125, 111, 100, 96, 95]
group_b = [100, 98, 61, 62, 125, 111, 100, 96, 95, 99, 92, 91, 96, 75, 114, 98, 89, 87, 125, 111]
group_c = [100, 98, 61, 69, 70, 81, 83, 86, 96, 87, 80, 89, 125, 111, 100, 96, 95, 94, 93, 89]
group_d = [126, 122, 86, 88, 92, 70, 84, 81, 89, 100, 140, 131, 120, 61, 62, 63, 64, 66, 76, 86]


plots = [(group_a, group_b, 'blue',   'A', 'B'),
         (group_a, group_c, 'green',  'A', 'C'),
         (group_a, group_d, 'red',    'A', 'D'),
         (group_b, group_c, 'purple', 'B', 'C')]

plt.figure(figsize=(12, 8), dpi=150)

for i in range(4):
    x, y, color, xn, yn = plots[i]
    plt.subplot(2, 2, i + 1)
    plt.scatter(x, y, color=color)
    plt.xlabel('Group ' + xn)
    plt.ylabel('Group ' + yn)
    plt.title('Group ' + xn + ' vs Group ' + yn)

plt.tight_layout()
plt.show()
