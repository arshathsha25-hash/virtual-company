import seaborn as sns
import pandas as pd

#load the data set using seaborn
df=sns.load_dataset("titanic")
#pandas methods/functions

#basic shape 
print("===shape===")
print(f"rows:{df.shape[0]},columns:{df.shape[1]}")


#column name data types

print("\n === column names&types ===")
print(df.dtypes)

#missing values 
print("\n\nmissing values")
print(df.isnull().sum())

#first 5 rows

print("\n\nfirst five rows")
print(df.head())
