#
# Regina
# Pandas test
#

import pandas as pd

# 1. Input
raw_data = pd.read_csv('Menu.csv')
print(raw_data)
print(raw_data.info())

# 2. Process
# total = raw_data['Price'].sum()
# print(total)

# print(raw_data['Price'].var())
# print(raw_data['Price'].std())

print(raw_data['Price'].sort_values()) 
print(raw_data.sort_values('Price')) 
print(raw_data.sort_values('Price', ascending=False)) 

# 3. Output 
