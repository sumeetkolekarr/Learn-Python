# =============================================================
# Seaborn
# Install first:  pip install seaborn
#
# Seaborn is built on top of Matplotlib and is specialized for
# statistical plots - far less code for common DS charts like
# distributions, correlations, and category comparisons.
# =============================================================
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Seaborn ships a few sample datasets - handy for practice
tips = sns.load_dataset("tips")
print(tips.head())

# -------------------------------------------------------------
# 1) Distribution plot
# -------------------------------------------------------------
sns.histplot(tips["total_bill"], kde=True)
plt.title("Distribution of Total Bill")
plt.show()

# -------------------------------------------------------------
# 2) Categorical comparison
# -------------------------------------------------------------
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Total Bill by Day")
plt.show()

# -------------------------------------------------------------
# 3) Correlation heatmap - one of the most-used DS visuals
# -------------------------------------------------------------
numeric_cols = tips.select_dtypes(include="number")
sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------------------------------------
# 4) Scatter with a trend line
# -------------------------------------------------------------
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=tips)
plt.title("Tip vs Total Bill")
plt.show()


# -------------------------------------------------------------
# Practice problems - solve these yourself
# -------------------------------------------------------------
# TODO Q1: Load the Titanic dataset (sns.load_dataset("titanic")
# also works) and plot survival rate by passenger class using
# sns.barplot.

# TODO Q2: Plot a correlation heatmap for the Titanic dataset's
# numeric columns and identify the two most correlated features.

# TODO Q3: Use sns.pairplot on the `tips` dataset to see
# relationships between all numeric columns at once.
