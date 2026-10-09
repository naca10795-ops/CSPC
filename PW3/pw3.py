# PW3 — Session 1: Heart Disease Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# TASK 1: Load and inspect the data
heart = pd.read_csv("PW3/heart.csv")

print("Dataset shape:")
print(heart.shape)

print("\nFirst five rows:")
print(heart.head())

print("\nSummary statistics:")
print(heart[["age", "chol", "trestbps", "thalach"]].describe())


# TASK 2: Plot histograms
columns = ["age", "chol", "trestbps", "thalach"]

for column in columns:
    plt.figure(figsize=(8, 5))

    sns.histplot(data=heart, x=column, bins=20, kde=True)

    plt.title("Distribution of " + column)
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("PW3/" + column + "_histogram.png")
    plt.show()


# TASK 3: Plot boxplots
for column in columns:
    plt.figure(figsize=(8, 4))

    sns.boxplot(data=heart, x=column)

    plt.title("Boxplot of " + column)
    plt.xlabel(column)

    plt.tight_layout()
    plt.savefig("PW3/" + column + "_boxplot.png")
    plt.show()


# TASK 4: Check normality using Q-Q plots
for column in columns:
    plt.figure(figsize=(6, 6))

    stats.probplot(heart[column], dist="norm", plot=plt)

    plt.title("Q-Q plot of " + column)

    plt.tight_layout()
    plt.savefig("PW3/" + column + "_qqplot.png")
    plt.show()