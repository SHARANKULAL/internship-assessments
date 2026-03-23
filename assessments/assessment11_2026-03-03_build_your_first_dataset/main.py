import pandas as pd

# Load dataset
df = pd.read_csv("study_hours_marks.csv")

print("Dataset:")
print(df)

print("\nCorrelation between Study Hours and Marks:")
print(df.corr(numeric_only=True))

print("\nMean Study Hours:", df["Study_Hours"].mean())
print("Mean Marks:", df["Marks"].mean())
