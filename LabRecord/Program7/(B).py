import pandas as pd

df= pd.read_csv("6Mcd_null_values.csv")

print("Original DataFrame:")
df

print("\nMissing values in the DataFrame:")
print(df.isnull().sum())
df['Q1'].fillna(df['Q1'].mean(), inplace=True)

print("\nDataFrame after filling missing values in 'Q1' column:")
df
