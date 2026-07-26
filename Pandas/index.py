# =============================================================
# Pandas
# Install first:  pip install pandas
#
# Why this matters: this is where most real day-to-day data
# science work happens - loading, cleaning, and reshaping data
# before any modeling or visualization.
# =============================================================
import pandas as pd

# -------------------------------------------------------------
# 1) Series vs DataFrame
# -------------------------------------------------------------
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

df = pd.DataFrame({
    "name": ["Amit", "Sara", "Sumeet", "Priya"],
    "age": [25, 30, 22, 28],
    "city": ["Mumbai", "Delhi", "Pune", "Bengaluru"],
})
print(df)


# -------------------------------------------------------------
# 2) Reading data
# Download any CSV (e.g. Titanic dataset from Kaggle) and place
# it next to this file, then uncomment:
# -------------------------------------------------------------
# titanic = pd.read_csv("titanic.csv")
# print(titanic.head())
# print(titanic.info())
# print(titanic.describe())


# -------------------------------------------------------------
# 3) Indexing / filtering
# -------------------------------------------------------------
print(df.loc[0])            # row by label
print(df.iloc[0])           # row by position
print(df[df["age"] > 25])   # boolean filtering, same idea as NumPy


# -------------------------------------------------------------
# 4) Cleaning
# -------------------------------------------------------------
messy = pd.DataFrame({"score": [90, None, 75, None, 60]})
print(messy.isna())
print(messy.fillna(messy["score"].mean()))
print(messy.dropna())


# -------------------------------------------------------------
# 5) groupby + aggregation
# -------------------------------------------------------------
sales = pd.DataFrame({
    "region": ["North", "South", "North", "South", "East"],
    "amount": [100, 200, 150, 300, 90],
})
print(sales.groupby("region")["amount"].sum())


# -------------------------------------------------------------
# 6) merge / join
# -------------------------------------------------------------
employees = pd.DataFrame({"emp_id": [1, 2, 3], "name": ["A", "B", "C"]})
salaries = pd.DataFrame({"emp_id": [1, 2, 3], "salary": [50000, 60000, 55000]})
print(pd.merge(employees, salaries, on="emp_id"))


# -------------------------------------------------------------
# Practice problems - solve these yourself
# -------------------------------------------------------------
# TODO Q1: Download the Titanic dataset (Kaggle), load it, and
# find the survival rate grouped by passenger class.

# TODO Q2: In the same dataset, fill missing "Age" values with
# the median age instead of dropping those rows.

# TODO Q3: Using the `sales` DataFrame above, find which region
# has the highest average sale amount (not just total).

# TODO Q4: Create a pivot_table from the Titanic dataset showing
# average fare by class and sex.
