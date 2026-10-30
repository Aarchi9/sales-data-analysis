import pandas as pd

df = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 102, 106, 107],
    "product": [
        "Laptop", "Phone", "laptop", "Tablet",
        "Phone", "Phone", "Laptop", "Tablet"
    ],
    "quantity": [2, 1, 3, 2, None, 1, -1, 4],
    "unit_price": [50000, 20000, 50000, 15000, 20000, 20000, 50000, None],
    "city": [
        "Ahmedabad", "Mumbai", "Ahmedabad", "Delhi",
        "Mumbai", "Mumbai", "Delhi", "Ahmedabad"
    ]
})
print(df)
print(df.shape) #-> number of rows and columns
df.info() #-> col names,non-null counts,datatypes,memory usage
print(df.dtypes) #-> datatype of each col
print(df.isnull().sum())# -> no. of missing values in each col 
print(df.duplicated().sum()) #->(counts exact duplicate rows)1 means there is one exact duplicated row in the entire dataframe
df[df["order_id"] ==102] #-> display all rows with order id 102
print(df[df["order_id"] == 102].duplicated().sum()) #-> checks if selected row contain exact duplicate
df = df.drop_duplicates()
df["product"]=df["product"].str.strip().str.lower()
print(df["product"].unique()) #-> unique helps to discover inconsistent values, it doesn't clean them automatically
print(df["product"].value_counts()) # -> to see how frequently each value appears
print(df["city"].value_counts())
suspicious = (df["quantity"].isna() )| (df["quantity"] <= 0) | (df["unit_price"].isna())
print(df[suspicious])
valid = (df["quantity"] > 0) & (df["unit_price"].notna())
print(df[valid])
valid_df = df[valid].copy()
valid_df["revenue"] = valid_df["quantity"]* valid_df["unit_price"]
print(valid_df)

#analyze sales by product
sales = valid_df.groupby("product")["revenue"].sum()
print(sales.sort_values(ascending=False))

#export sales report to csv
sales_report = sales.reset_index()
sales_report = sales_report.rename(columns = {"revenue": "total_revenue"})
sales_report.to_csv("sales_report.csv",index = False)