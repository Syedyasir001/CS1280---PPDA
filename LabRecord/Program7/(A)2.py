import pandas as pd
df=pd.read_csv('1experience.csv')

print("First 6 rows of the Dataframe:")
print(df.head(6))

print("\nColumn names data types:")
print(df.info())
