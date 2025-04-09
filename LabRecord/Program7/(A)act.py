import pandas as pd
products = [
    {"Product Name": "Laptop", "Category": "Electronics", "Price": 60000},
    {"Product Name": "T-Shirt", "Category": "Clothing", "Price": 800},
    {"Product Name": "Smartphone", "Category": "Electronics", "Price": 25000},
    {"Product Name": "Book", "Category": "Stationery", "Price": 400},
    {"Product Name": "Shoes", "Category": "Footwear", "Price": 2000}
]
df = pd.DataFrame(products)
df["Discounted Price"] = df["Price"] * 0.9

print(df)
