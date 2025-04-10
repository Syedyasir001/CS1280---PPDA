import pandas as pd
import numpy as np

df = pd.read_csv('2Salary.csv')

description = df['YearsExperience'].describe()
quantiles = df['YearsExperience'].quantile([0.25, 0.5, 0.75])

skewness = df['YearsExperience'].skew()
kurtosis = df['YearsExperience'].kurt()

print("Statistical Summary:\n", description)
print("\nQuantiles:\n", quantiles)
print("\nSkewness:", skewness)
print("Kurtosis:", kurtosis)
