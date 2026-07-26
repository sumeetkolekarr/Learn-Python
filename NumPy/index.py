# =============================================================
# NumPy
# Install first:  pip install numpy
#
# Why this matters: NumPy arrays are the foundation Pandas,
# scikit-learn, and every deep learning framework are built on.
# The key mental shift from plain Python: operate on WHOLE
# arrays at once instead of looping element by element.
# =============================================================
import numpy as np

# -------------------------------------------------------------
# 1) Creating arrays
# -------------------------------------------------------------
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((2, 3))
c = np.arange(0, 10, 2)
d = np.linspace(0, 1, 5)
print(a, b, c, d, sep="\n")


# -------------------------------------------------------------
# 2) Vectorized math (the mindset shift)
# Instead of: for i in range(len(a)): a[i] * 2
# -------------------------------------------------------------
print(a * 2)
print(a + a)
print(a > 2)          # boolean array
print(a[a > 2])       # boolean masking - select where condition is True


# -------------------------------------------------------------
# 3) Shape, reshape, axis
# axis=0 -> down the rows (per column), axis=1 -> across columns (per row)
# -------------------------------------------------------------
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)
print(matrix.reshape(3, 2))
print(matrix.sum(axis=0))
print(matrix.sum(axis=1))


# -------------------------------------------------------------
# 4) Broadcasting
# NumPy automatically expands smaller arrays to match shapes
# when the dimensions are compatible.
# -------------------------------------------------------------
prices = np.array([100, 200, 300])
discount = 0.1
print(prices * (1 - discount))


# -------------------------------------------------------------
# 5) Random numbers (used constantly for sampling/simulation)
# -------------------------------------------------------------
rng = np.random.default_rng(seed=42)
print(rng.integers(1, 100, size=5))
print(rng.normal(loc=0, scale=1, size=5))


# -------------------------------------------------------------
# Practice problems - solve these yourself
# -------------------------------------------------------------
# TODO Q1: Create a 1D array of numbers 1-20 and select only the
# multiples of 3 using boolean masking (no loops).

# TODO Q2: Create a 4x4 matrix of random integers between 1-100.
# Find the row sums and column sums.

# TODO Q3: Given prices = np.array([250, 400, 999, 120]), compute
# the price after applying an 18% tax, rounded to 2 decimals.

# TODO Q4: Create two 3x3 matrices and compute their matrix
# product using np.dot (not element-wise multiplication).
