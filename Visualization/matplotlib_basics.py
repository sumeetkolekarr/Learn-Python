# =============================================================
# Matplotlib basics
# Install first:  pip install matplotlib
#
# The confusing part at first is the Figure/Axes model:
# - Figure = the whole window/canvas
# - Axes   = one plot inside that canvas (you can have several)
# =============================================================
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------------------
# 1) A basic line plot
# -------------------------------------------------------------
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="sin(x)")
ax.set_title("Basic Line Plot")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.legend()
plt.show()


# -------------------------------------------------------------
# 2) Multiple plots in one figure (subplots)
# -------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x, np.sin(x))
axes[0].set_title("sin(x)")
axes[1].plot(x, np.cos(x))
axes[1].set_title("cos(x)")
plt.tight_layout()
plt.show()


# -------------------------------------------------------------
# 3) Bar chart and histogram - the two most common DS plots
# -------------------------------------------------------------
categories = ["A", "B", "C", "D"]
values = [23, 45, 12, 38]

plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()

data = np.random.normal(loc=50, scale=10, size=1000)
plt.hist(data, bins=30)
plt.title("Histogram")
plt.show()


# -------------------------------------------------------------
# Practice problems - solve these yourself
# -------------------------------------------------------------
# TODO Q1: Plot y = x^2 and y = x^3 on the same axes with a
# legend, for x from -10 to 10.

# TODO Q2: Create a 2x2 grid of subplots showing sin, cos, tan,
# and a histogram of random data.

# TODO Q3: Load the Titanic dataset (from the Pandas folder) and
# plot a bar chart of passenger count per class.
