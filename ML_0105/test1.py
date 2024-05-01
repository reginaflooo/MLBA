import pandas as pd

df = pd.read_csv('data.csv')

# 1. Cleaning Data: 

# 1.1 Cleaning Empty Cells
# Returning a new Data Frame with no empty cells
new_df = df.dropna()
print(new_df.to_string())

# Removing all rows with NULL values
df.dropna(inplace = True)
print(df.to_string())

# Replace the NULL values with the value/number 130 
df.fillna(130, inplace = True)

# Replace the NULL values in the "Calories" column with the number 130
df['Calories'].fillna(130, inplace = True)

# Replace NULL values with statistical calculations: mean, median, mode
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)

x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)

# 1.2 Cleaning Wrong Formats 
# Date formats 
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())

df.dropna(subset=['Date'], inplace = True) # since there is an observation where the Date is null

# 1.3 Cleaning Wrong Data
# Directly replacing values 
df.loc[7, 'Duration'] = 45 # df.loc locates the object on the 7th row (*numbering start from 0) of the 'Duration' column

# Replacing the values of 'Duration' where it exceed the value 120 
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

# Deleting the values of 'Duration' where it exceed the value 120
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

# 1.4 Removing Duplicates 
print(df.duplicated()) # returns True for every row that is a duplicate, and False for not

df.drop_duplicates(inplace = True)
print(df.duplicated())
