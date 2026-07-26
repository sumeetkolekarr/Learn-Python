# =============================================================
# Math & Stats for Data Science - in code, not by hand
# Install first:  pip install numpy scipy pandas
#
# Goal: not a full math course - just enough to not be lost
# when AI/DS material talks about distributions, correlation,
# or vectors/matrices.
# =============================================================
import numpy as np
from scipy import stats
import pandas as pd

# -------------------------------------------------------------
# 1) Descriptive statistics
# -------------------------------------------------------------
data = np.array([12, 15, 12, 18, 20, 22, 25, 25, 30, 100])  # note the outlier

print("mean:", np.mean(data))
print("median:", np.median(data))     # less sensitive to the outlier than mean
print("std:", np.std(data))
print("variance:", np.var(data))

df = pd.Series(data)
print(df.describe())


# -------------------------------------------------------------
# 2) Correlation
# -------------------------------------------------------------
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8])
scores = np.array([50, 55, 65, 70, 72, 80, 85, 95])
correlation = np.corrcoef(hours_studied, scores)[0, 1]
print("correlation:", correlation)


# -------------------------------------------------------------
# 3) Probability distributions (scipy.stats)
# -------------------------------------------------------------
# Normal distribution: probability density at a point
print(stats.norm.pdf(0, loc=0, scale=1))

# Generate samples from a normal distribution
samples = stats.norm.rvs(loc=50, scale=10, size=1000, random_state=42)
print("sample mean:", samples.mean())

# A simple hypothesis test: is the sample mean significantly
# different from 50?
t_stat, p_value = stats.ttest_1samp(samples, popmean=50)
print("t-stat:", t_stat, "p-value:", p_value)


# -------------------------------------------------------------
# 4) Vectors & matrices (linear algebra basics)
# This is literally what neural networks are built from -
# inputs and weights are vectors/matrices, and a "forward pass"
# is repeated matrix multiplication.
# -------------------------------------------------------------
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print("dot product:", np.dot(v1, v2))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("matrix product:\n", A @ B)
print("transpose:\n", A.T)
print("inverse:\n", np.linalg.inv(A))


# -------------------------------------------------------------
# Practice problems - solve these yourself
# -------------------------------------------------------------
# TODO Q1: Given a dataset with an outlier, compare how much the
# mean shifts vs the median when you remove the outlier.

# TODO Q2: Generate 1000 samples from a normal distribution and
# plot a histogram (reuse matplotlib_basics.py) to visually
# confirm the bell curve shape.

# TODO Q3: Given two vectors representing a student's marks in
# two subjects across a class, compute their correlation and
# interpret what a value close to 1, 0, or -1 would mean.

# TODO Q4: Multiply a 3x2 matrix by a 2x4 matrix and verify the
# resulting shape matches what matrix multiplication rules predict.
