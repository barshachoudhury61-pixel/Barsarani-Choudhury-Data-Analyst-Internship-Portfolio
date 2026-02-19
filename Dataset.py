import pandas as pd

customers = pd.DataFrame({
    "customer_id": range(1, 16),
    "name": [
        "Amit", "Riya", "Sohan", "Pooja", "Rahul",
        "Anita", "Vikash", "Neha", "Arjun", "Sneha",
        "Rohit", "Kiran", "Manish", "Priya", "Suman"
    ],
    "age": [22, 25, 30, 28, 35, 40, 27, 24, 32, 29, 45, 38, 33, 26, 50],
    "gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "F"],
    "city": ["Delhi", "Mumbai", "Pune", "Kolkata", "Bangalore",
             "Chennai", "Hyderabad", "Delhi", "Pune", "Mumbai",
             "Bangalore", "Chennai", "Hyderabad", "Delhi", "Kolkata"],
    "signup_date": pd.date_range(start="2023-01-01", periods=15, freq="15D")
})

customers.to_csv("customers.csv", index=False)
print("customers.csv created")


products = pd.DataFrame({
    "product_id": range(101, 111),
    "product_name": [
        "Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse",
        "Monitor", "Tablet", "Smartwatch", "Camera", "Printer"
    ],
    "category": [
        "Electronics", "Electronics", "Accessories", "Accessories",
        "Accessories", "Electronics", "Electronics", "Wearables",
        "Electronics", "Electronics"
    ],
    "price": [60000, 30000, 2000, 1500, 800, 12000, 25000, 8000, 45000, 10000]
})

products.to_csv("products.csv", index=False)
print("products.csv created")


orders = pd.DataFrame({
    "order_id": range(1001, 1021),
    "customer_id": [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        1, 3, 5, 7, 9
    ],
    "order_date": pd.date_range(start="2023-06-01", periods=20, freq="7D"),
    "total_amount": [
        62000, 32000, 45000, 28000, 80000,
        15000, 22000, 18000, 55000, 40000,
        30000, 20000, 70000, 35000, 90000,
        25000, 48000, 60000, 27000, 52000
    ]
})

orders.to_csv("orders.csv", index=False)
print("orders.csv created")
