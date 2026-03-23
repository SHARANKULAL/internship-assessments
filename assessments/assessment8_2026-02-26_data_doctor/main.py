import pandas as pd

df = pd.read_csv("dataset.csv")

print("Original Dataset:")
print(df.head())

# 1. Handle Missing Values
df = df.ffill()

# 2. Remove Duplicate Rows
df = df.drop_duplicates()

# 3. Standardize Text
df.columns = df.columns.str.strip().str.lower()

for col in df.select_dtypes(include='object'):
    df[col] = df[col].str.strip().str.lower()

print("\nCleaned Dataset:")
print(df.head())

df.to_csv("cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved as cleaned_dataset.csv")
