#
# Regina
# Pandas practice
# 

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('smoker1.csv')

print(df)

# Inspecting the data (missing values, etc.)
df.shape 
df.info()

# Visualize : What is the distribution of the smokers?
df['smoker'].hist()
plt.show()

# Count the distribution of a focus column 
df['smoker'].value_counts()
df['treatment'].value_counts()
df['outcome'].value_counts()

# Calculating the mean for each  column 
df['smoker'].mean()
df['treatment'].mean()
df['outcome'].mean()

# In pandas, axis = 0 refers to the HORIZONTAL AXIS (act on ALL THE ROWS in EACH COLUMN)
# While axis = 1 refers to the VERTICAL AXIS (act on ALL THE COLUMNS in EACH ROWS)

# Sum 
df.sum() # calculate the sum of each variables (columns) seperately
df.sum(axis = 1) # calculate the sum of all the columns for each rows

df.describe() # outputs the basic statistical information 

# Selection 
df['smoker'] # selecting all the rows of column 'smoker'
df[0:3] # selecting all the columns from row index 0 until row index 3-1 (or 2) 
# df[x:y+1] where x is the starting index of the row and y is the desired ending index of the row

df.loc[0:3, 'smoker'] # selecting the column 'smoker' from rows from index 0 to index 3 
df.iloc[1,0] # selecting the object on row index 1 of column index 0
