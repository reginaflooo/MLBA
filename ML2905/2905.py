# Import packages 
import pandas as pd
import seaborn as sns
import matplotlib as plt 
import plotly as ply

# Importing the data
df = sns.load_dataset('iris')

# Exploring the dataset
df.head()
    # Looking at the dataset to get a general picture
df.info()
    # The dataset has 150 observations with 5 columns. Each column does not have null values
    # All columns except for 'species' have a float data type, and the latter has an object type
df.describe()
    # We obtain the general statistics information about the four numerical data

# Cleaning Data
df2 = df.drop_duplicates()
df2

# Analysis and Visualization 
# 1. Scatterplot: comparison of sepal length and sepal width
sns.scatterplot(data = df2, x = "sepal_length", y = "sepal_width",
                hue = "species")

plt.title("Comparison of Sepal Width and Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.show()

# 2. Scatterplot: comparison of petal length and petal width
sns.scatterplot(data = df2, x = "petal_length", y = "petal_width",
                hue = "species")

plt.title("Comparison of Petal Width and Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.show()

# 3. Correlation between variables 
df2.corr()
    # From this, we can generally see the correlation between the variables (columns)
    # Some noticable correlation occurs in the petal length & petal width, as well as petal length & sepal length

sns.heatmap(df2.corr())
plt.show()