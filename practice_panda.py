import pandas as pd

my_data = pd.read_csv("Data.csv")

print(my_data)
print(my_data.info())

# Dropping null values
my_data = my_data.dropna() 
print(my_data.info())

# Re-formatting the dates 
my_data['Date'] = pd.to_datetime(my_data['Date'], format='mixed')
print(my_data)

# Changing the value of 'Duration' on the 7th observaton or row into a new value
my_data.loc[7, 'Duration']=45 
print(my_data)


