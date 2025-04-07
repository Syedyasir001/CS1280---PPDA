import pandas as pd

df = pd.read_csv("1experience.csv")

print("1. Last three rows of the DataFrame:")
print(df.tail(3))

print("2. Description of the DataFrame:")
print(df.describe())

print("   Information of the DataFrame:")
df.info()

print("3. Column Names:")
print(df.columns.tolist())
