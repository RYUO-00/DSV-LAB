import matplotlib.pyplot as plt

iq_scores = [126, 89, 90, 101, 102, 106, 93, 101, 116, 120,
             108, 97, 98, 105, 89, 110, 71, 90, 89, 70]
group_a = [118, 123, 125, 107, 111, 96, 104, 96, 75, 114, 87, 117, 119, 112, 107, 102, 93, 94, 108, 98]
group_b = [105, 128, 99, 105, 98, 126, 109, 93, 94, 119, 112, 107, 97, 98, 84, 96, 80, 96, 75, 114]
group_c = [108, 89, 119, 116, 104, 113, 96, 69, 121, 107, 102, 122, 104, 107, 108, 137, 107, 116, 98, 132]
group_d = [93, 99, 91, 110, 80, 113, 111, 115, 98, 74, 96, 80, 83, 102, 60, 91, 82, 90, 97, 101]

# 1. Histogram
plt.figure(figsize=(6, 4), dpi=150)
plt.hist(iq_scores, bins=10, color='gray', edgecolor='black')
plt.axvline(x=100, color='r')
plt.axvline(x=85, color='r', linestyle='--')
plt.xlabel('IQ score')
plt.ylabel('Frequency')
plt.title('IQ scores for a test group of a hundred adults')
plt.show()

# 2. Box plot of one group
plt.figure(figsize=(6, 4), dpi=150)
plt.boxplot(iq_scores)
plt.gca().set_xticklabels(['Test group'])
plt.ylabel('IQ score')
plt.title('IQ scores for a test group of a hundred adults')
plt.show()

# 3. Box plot of four groups
plt.figure(figsize=(6, 4), dpi=150)
plt.boxplot([group_a, group_b, group_c, group_d])
plt.gca().set_xticklabels(['Group A', 'Group B', 'Group C', 'Group D'])
plt.ylabel('IQ score')
plt.title('IQ scores for different test groups')
plt.show()
