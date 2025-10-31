import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# save as csv

path = "pandas/people.csv"
df.to_csv(path, index=False)
print("csv file saved.")

# read from csv

df2 = pd.read_csv(path)
print(df2)  # Display the DataFrame read from CSV

# single column

print(df["Name"])  # Accessing 'Name' column

# Basics operations

print(df.describe())  # Summary statistics
print(df.info())      # DataFrame info
print(df.head(2))    # First 2 rows
print(df.tail(2))    # Last 2 rows
print(df.sort_values(by="Age"))  # Sort by Age
print(df[df["Age"] > 28])  # Filter rows where Age > 28
print(df.groupby("City").size())  # Group by City and count
print(df.isnull().sum())  # Check for null values

# add new column
df["Salary"] = [70000, 80000, 90000]
print(df)  # Display DataFrame with new Salary column
