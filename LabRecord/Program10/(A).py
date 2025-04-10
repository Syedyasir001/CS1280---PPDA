import pandas as pd
df = pd.read_csv('4laptops.csv')
df

pd.get_dummies(df)
from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder()
enc_data = enc.fit_transform(df[['Category']])
enc_data 

enc.categories_
enc_data.toarray()

#creating a dataframe without giving column names
enc_df = pd.DataFrame(enc_data.toarray())
enc_df

# creating a dataframe with giving column names
enc_df = pd.DataFrame(enc_data.toarray(), columns=['2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation'])
enc_df
df1 = df.join(enc_df) # joining df and enc_df
df1

# Using label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

# Fit and transform the data
df['RAM'] = le.fit_transform(df['RAM'])
df

le.classes_
