# =============================================================
# Intro to ML (scikit-learn)
# Install first:  pip install scikit-learn pandas
#
# This is intentionally light - the goal isn't to master ML yet,
# it's to see how everything from the folders above (NumPy,
# Pandas, Math/Stats) feeds into one standard workflow:
#   load data -> split -> fit -> predict -> evaluate
# =============================================================
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.datasets import load_iris

# -------------------------------------------------------------
# 1) Linear Regression - predicting a number
# -------------------------------------------------------------
# Fake data: hours studied -> exam score
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([50, 55, 65, 70, 72, 80, 85, 95])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("predictions:", predictions)
print("actual:", y_test)
print("mean squared error:", mean_squared_error(y_test, predictions))


# -------------------------------------------------------------
# 2) Classification - predicting a category
# Using the classic Iris dataset (built into sklearn)
# -------------------------------------------------------------
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
preds = clf.predict(X_test)

print("accuracy:", accuracy_score(y_test, preds))


# -------------------------------------------------------------
# Practice problems - solve these yourself
# -------------------------------------------------------------
# TODO Q1: Load the Titanic dataset (from the Pandas folder),
# pick a few numeric features (age, fare, pclass), and train a
# LogisticRegression model to predict survival. Report accuracy.

# TODO Q2: Try DecisionTreeClassifier instead of
# LogisticRegression on the same Titanic features - does
# accuracy change?

# TODO Q3: Using the Iris example above, try changing
# test_size and random_state - notice how accuracy varies. Why
# does that happen?
