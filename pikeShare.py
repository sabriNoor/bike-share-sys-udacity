import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("chicago.csv")

# Check column names
print("Columns:", df.columns)

# Check for missing values in each column
print("Missing values in each column:")
print(df.isnull().sum())

# Check data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Get unique values in each column (this may be slow for large datasets)
print("\nUnique values in each column:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# If you want to see specific examples of unique values in each column
print("\nExample unique values for each column:")
for col in df.columns:
    print(f"{col}: {df[col].unique()[:5]}")  # Showing first 5 unique values as an example


# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

## extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

## find the most popular hour
popular_hour = df['hour'].mode()[0]
    
print('Most Popular Start Hour:', popular_hour)


# print value counts for each user type User Type
user_types = df['User Type'].value_counts()
print(user_types)
