import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

print("----- Top 5 Rows -----")
print(df.head())

max_values = df.max(numeric_only=True)
highest_column = max_values.idxmax()
highest_value = max_values.max()

print("\nColumn with Highest Maximum Value:")
print("Column:", highest_column)
print("Value:", highest_value)

print("\n----- Missing Values -----")
print(df.isnull().sum())

print("\n----- Statistical Summary -----")
print(df.describe())
