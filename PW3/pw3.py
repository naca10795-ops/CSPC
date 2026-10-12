# PW3 — Session 1: Heart Disease Dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# TASK 1: Load and inspect the data
heart = pd.read_csv("heart.csv")

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
    plt.savefig(column + "_histogram.png")
    plt.show()


# TASK 3: Plot boxplots
for column in columns:
    plt.figure(figsize=(8, 4))

    sns.boxplot(data=heart, x=column)

    plt.title("Boxplot of " + column)
    plt.xlabel(column)

    plt.tight_layout()
    plt.savefig(column + "_boxplot.png")
    plt.show()


# TASK 4: Check normality using Q-Q plots
for column in columns:
    plt.figure(figsize=(6, 6))

    stats.probplot(heart[column], dist="norm", plot=plt)

    plt.title("Q-Q plot of " + column)

    plt.tight_layout()
    plt.savefig(column + "_qqplot.png")
    plt.show()

# TASK 5: Shapiro-Wilk Test & Verdict Record
print("SHAPIRO-WILK NORMALITY TEST RESULTS")

verdicts = {}

for column in columns:
    # I run the Shapiro-Wilk test
    stat, p_value = stats.shapiro(heart[column])

    # Interpret p-value (alpha = 0.05)
    # If p > 0.05 -> Normal distribution
    # If p <= 0.05 -> Not normal distribution
    is_normal = p_value > 0.05
    verdict = "Approximately Normal" if is_normal else "Not Normal"

    verdicts[column] = {
        "Statistic": round(stat, 4),
        "p-value": round(p_value, 5),
        "Verdict": verdict,
    }

    print(
        f"Variable: {column:10s} | W-Stat: {stat:.4f} | p-value: {p_value:.5f} | Verdict: {verdict}"
    )

# Summary DataFrame
results_df = pd.DataFrame(verdicts).T
print("\nFinal Summary Table:")
print(results_df)

# Session 2 — Is the effect real?

# Separate patients into two groups
disease = heart[heart["target"] == 1]
healthy = heart[heart["target"] == 0]

# Calculate mean maximum heart rate for each group
mean_disease = disease["thalach"].mean()
mean_healthy = healthy["thalach"].mean()

print("\nTASK 4: Maximum Heart Rate Comparison")
print("Patients with heart disease:")
print("Number of patients:", len(disease))
print("Mean maximum heart rate:", round(mean_disease, 2))

print("\nPatients without heart disease:")
print("Number of patients:", len(healthy))
print("Mean maximum heart rate:", round(mean_healthy, 2))

# Mann-Whitney U test
u_statistic, p_value = stats.mannwhitneyu(
    disease["thalach"],
    healthy["thalach"],
    alternative="two-sided"
)

print("\nMANN-WHITNEY U TEST")
print("U statistic:", round(u_statistic, 2))
print("p-value:", p_value)

# Interpreting the result
alpha = 0.05

if p_value < alpha:
    print("Conclusion: The difference is statistically significant.")
else:
    print("Conclusion: There is insufficient evidence of a difference.")

# TASK 4: Uncertainty estimates and comparison plot

# Calculating standard error for each group
sem_disease = stats.sem(disease["thalach"])
sem_healthy = stats.sem(healthy["thalach"])

# Calculating approximate 95% confidence intervals
low_disease = mean_disease - 2 * sem_disease
high_disease = mean_disease + 2 * sem_disease

low_healthy = mean_healthy - 2 * sem_healthy
high_healthy = mean_healthy + 2 * sem_healthy

print("\nMEANS WITH STANDARD ERRORS")
print(
    f"Heart disease: {mean_disease:.2f} "
    f"+/- {sem_disease:.2f} bpm"
)
print(
    f"No heart disease: {mean_healthy:.2f} "
    f"+/- {sem_healthy:.2f} bpm"
)

print("\nAPPROXIMATE 95% CONFIDENCE INTERVALS")

print(
    f"Heart disease: [{low_disease:.2f}, {high_disease:.2f}] bpm"
)

print(
    f"No heart disease: [{low_healthy:.2f}, {high_healthy:.2f}] bpm"
)

# Ploting group means with standard error bars
means = [mean_disease, mean_healthy]
errors = [sem_disease, sem_healthy]
labels = ["Heart disease", "No heart disease"]

plt.figure(figsize=(8, 5))

plt.bar(
    labels,
    means,
    yerr=errors,
    capsize=8
)

plt.title("Mean Maximum Heart Rate by Heart Disease Status")
plt.xlabel("Patient group")
plt.ylabel("Mean maximum heart rate (bpm)")
plt.tight_layout()

plt.savefig("thalach_group_comparison.png")
plt.show()

# TASK 5: Relationship between age and maximum heart rate

# Calculate Pearson correlation
correlation, p_value = stats.pearsonr(
    heart["age"],
    heart["thalach"]
)

print("\nTASK 5: AGE AND MAXIMUM HEART RATE")
print("Pearson correlation:", round(correlation, 4))
print("p-value:", p_value)

if p_value < 0.05:
    print("The correlation is statistically significant.")
else:
    print("The correlation is not statistically significant.")

# Scatter plot
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=heart,
    x="age",
    y="thalach"
)

plt.title("Age vs Maximum Heart Rate")
plt.xlabel("Age (years)")
plt.ylabel("Maximum heart rate (bpm)")
plt.tight_layout()

plt.savefig("age_thalach_scatter.png")
plt.show()

# TASK 6: Inspect the chemicals and cancer dataset

chemicals = pd.read_csv("chemicals_cancer.csv")

print("\nTASK 6: CHEMICALS AND CANCER DATASET")
print("Dataset shape:", chemicals.shape)

print("\nFirst five rows:")
print(chemicals.head())

print("\nColumn names:")
print(chemicals.columns.tolist())

# TASK 6: Correlations with malignancy

print("\nCORRELATIONS WITH MALIGNANCY")

variables = [
    "benzene",
    "cadmium",
    "pollution_index",
    "age"
]

for variable in variables:
    correlation, p_value = stats.pearsonr(
        chemicals[variable],
        chemicals["malignancy"]
    )

    print(
        f"{variable:16s} | "
        f"Correlation: {correlation:.4f} | "
        f"p-value: {p_value:.6e}"
    )

# TASK 7: CONTROL FOR POLLUTION INDEX

# Select patients with a pollution index between 40 and 60.

similar_pollution = chemicals[
    (chemicals["pollution_index"] > 40)
    & (chemicals["pollution_index"] < 60)
]

print("\nTASK 7: CONTROLLING FOR POLLUTION INDEX")
print("Number of patients:", len(similar_pollution))

# Calculate the correlations within this group.
for chemical in ["benzene", "cadmium"]:
    correlation, p_value = stats.pearsonr(
        similar_pollution[chemical],
        similar_pollution["malignancy"]
    )

    print(f"\n{chemical.capitalize()}:")
    print("Correlation:", round(correlation, 4))
    print("p-value:", p_value)

# BONUS TASK: ENTROPY OF HEART DISEASE TARGET

# Calculate the proportion of each category
probabilities = heart["target"].value_counts(normalize=True)

print("\nBonus Task: Entropy")
print("Category proportions:")
print(probabilities)

# Calculate entropy in bits
entropy = -(probabilities * np.log2(probabilities)).sum()

print("Entropy:", round(entropy, 4), "bits")
