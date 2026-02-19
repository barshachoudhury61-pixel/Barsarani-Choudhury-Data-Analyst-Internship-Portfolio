import pandas as pd

# Sales data
data = {
    "Order_ID": [1001, 1002, 1003, 1004],
    "Order_Date": ["2025-01-05", "2025-01-06", "2025-01-06", "2025-01-07"],
    "Customer_ID": [201, 202, 203, 204],
    "Customer_Name": ["Ravi", "Sita", "Amit", "Neha"],
    "Product": ["Laptop", "Mobile", "Headphones", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories"],
    "Quantity": [1, 2, 3, 2],
    "Unit_Price": [55000, 30000, 1500, 1200],
    "Region": ["North", "South", "East", "West"]
}

df = pd.DataFrame(data)

# Feature Engineering
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Save CSV
df.to_csv("sales_dataset.csv", index=False)
import pandas as pd

# Load CSV file
df = pd.read_csv("sales_dataset.csv")

# View first 5 rows
print(df.head())
# Dataset info
df.info()
# Statistical summary
df.describe()
# Missing values count
print(df.isnull().sum())
# Total duplicate rows
print("Duplicate rows:", df.duplicated().sum())
# View duplicate records
df[df.duplicated()]
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Region"].value_counts()
# Fix formatting
df["Region"] = df["Region"].str.strip().str.title()
Q1 = df["Total_Sales"].quantile(0.25)
Q3 = df["Total_Sales"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df["Total_Sales"] < Q1 - 1.5 * IQR) |
    (df["Total_Sales"] > Q3 + 1.5 * IQR)
]

print(outliers)