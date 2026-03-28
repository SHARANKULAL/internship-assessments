import pandas as pd

df = pd.read_csv("data.csv")

df = df.drop_duplicates()
df = df.fillna(0)
df.columns = df.columns.str.lower()

print(df.head())