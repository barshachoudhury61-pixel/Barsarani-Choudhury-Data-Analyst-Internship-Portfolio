import pandas as pd

# Create dataset
data = {
    "CustomerID": ["C001", "C002", "C003", "C001", "C004", "C005", "C006", "C002", "C007", "C008"],
    "OrderID": ["O1001", "O1002", "O1003", "O1004", "O1005", "O1006", "O1007", "O1008", "O1009", "O1010"],
    "OrderDate": [
        "2024-01-05", "2024-01-07", "2024-01-10", "2024-02-12",
        "2024-02-15", "2024-02-18", "2024-03-02", "2024-03-05",
        "2024-03-10", "2024-03-12"
    ],
    "SignupDate": [
        "2023-12-20", "2024-01-01", "2024-01-03", "2023-12-20",
        "2024-02-10", "2024-02-12", "2024-02-25", "2024-01-01",
        "2024-03-01", "2024-03-05"
    ],
    "Channel": ["Organic", "Paid Ads", "Referral", "Organic", "Organic", "Paid Ads", "Referral", "Paid Ads", "Organic", "Paid Ads"],
    "Product": ["Laptop", "Mouse", "Keyboard", "Headphones", "Laptop", "Mobile", "Tablet", "Charger", "Laptop", "Mouse"],
    "Category": ["Electronics", "Accessories", "Accessories", "Accessories", "Electronics", "Electronics", "Electronics", "Accessories", "Electronics", "Accessories"],
    "OrderValue": [55000, 800, 1500, 2500, 60000, 20000, 30000, 1200, 58000, 900],
    "OrderStatus": ["Completed", "Completed", "Completed", "Completed", "Cancelled", "Completed", "Completed", "Completed", "Completed", "Abandoned"],
    "Stage": ["Purchase", "Purchase", "Purchase", "Purchase", "Checkout", "Purchase", "Purchase", "Purchase", "Purchase", "Cart"],
    "Region": ["East", "South", "North", "East", "West", "South", "North", "South", "East", "West"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("ecommerce_dashboard_data.csv", index=False)

print("ecommerce_dashboard_data.csv created successfully!")
