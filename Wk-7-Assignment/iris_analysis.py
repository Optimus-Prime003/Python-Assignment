# Iris Dataset Analysis Assignment
# --------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    df['species'] = iris.target_names[iris.target]
    print("✅ Dataset loaded successfully!")
except Exception as e:
    print(f"❌ Error occurred: {e}")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Clean missing values (not needed for Iris, but included)
df = df.dropna()

# Task 2: Basic Data Analysis
print("\nSummary Statistics:")
print(df.describe())

print("\nMean values by species:")
print(df.groupby("species").mean(numeric_only=True))

print("\nObservation: Setosa generally has smaller sepal and petal sizes compared to Versicolor and Virginica.")

# Task 3: Data Visualization

# 1. Line Chart - sepal length trend
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="blue")
plt.title("Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart - Average petal length by species
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, palette="viridis")
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram - Sepal width distribution
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=20, color="orange", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - Sepal length vs Petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="deep")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()