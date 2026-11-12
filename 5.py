# Experiment 5: Non-parametric Locally Weighted Regression (LWR)
# Needs '10-dataset.csv' with columns 'total_bill' and 'tip' (the "tips" dataset).
# If the file is missing, dummy data is generated so the program still runs.
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def kernel(point, xmat, tau):
    """Gaussian weight of every training point with respect to 'point'."""
    m = len(xmat)
    weights = np.eye(m)                      # diagonal weight matrix
    for i in range(m):
        diff = point - xmat[i]
        weights[i, i] = np.exp(np.dot(diff, diff) / (-2.0 * tau ** 2))
    return weights


def locally_weighted_regression(xmat, ymat, tau):
    """Fit a separate weighted straight line around every point."""
    y_pred = np.zeros(len(xmat))
    for i in range(len(xmat)):
        weights = kernel(xmat[i], xmat, tau)
        # theta = (X^T W X)^-1 (X^T W y)
        theta = np.linalg.pinv(xmat.T @ weights @ xmat) @ (xmat.T @ weights @ ymat)
        y_pred[i] = xmat[i] @ theta
    return y_pred


# ---------- Load data ----------
if os.path.exists('10-dataset.csv'):
    data = pd.read_csv('10-dataset.csv')
else:
    print("10-dataset.csv not found, using dummy data")
    rng = np.random.default_rng(0)
    total = rng.uniform(5, 50, 150)
    data = pd.DataFrame({'total_bill': total,
                         'tip': 0.15 * total + rng.normal(0, 1, 150)})

bill = np.array(data['total_bill'])
tip = np.array(data['tip'])

# ---------- Build X (column of ones + bill) and y ----------
X = np.hstack((np.ones((len(bill), 1)), bill.reshape(-1, 1)))
y = tip

tau = 0.5
y_pred = locally_weighted_regression(X, y, tau)

# ---------- Plot ----------
sorted_indices = X[:, 1].argsort()   # sort by bill so the line is drawn left to right
plt.scatter(bill, tip, color='blue', label='Data Points')
plt.plot(X[sorted_indices, 1], y_pred[sorted_indices],
         color='red', label='LWR Prediction', linewidth=2)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.legend()
plt.title('Non-Parametric Locally Weighted Regression')
plt.show()
