import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read customer churn dataset
df = pd.read_csv("customer_churn.csv")

print("First 5 records:")
print(df.head())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Handle missing values
df = df.fillna(df.mean(numeric_only=True))

# Remove duplicate records
df = df.drop_duplicates()

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Mean
print("\nMean:")
print(df.mean(numeric_only=True))

# Maximum
print("\nMaximum:")
print(df.max(numeric_only=True))

# Minimum
print("\nMinimum:")
print(df.min(numeric_only=True))

# Churn count
print("\nChurn Count:")
print(df["Churn"].value_counts())

# Visualization
df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

print("\nEDA completed successfully.")