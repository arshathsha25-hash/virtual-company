import seaborn as sns
import pandas as pd

df=sns.load_dataset("titanic")

print(f"no of rows before duplicate:{len(df)}")

print(f"\n\n duplicate rows:{df.duplicated().sum()}")

#droping duplicates
df_clean=df.drop_duplicates()
print(f"data after droping duplicate:{len(df_clean)}")

#droping a entire column because it contains more than 70 % of missing data
df_clean=df_clean.drop(columns=["deck"])
df_clean=df_clean.dropna(subset=['embark_town'])

#fill age with medium 
medium_age=df_clean['age'].median()
df_clean['age']=df_clean['age'].fillna(medium_age)

#dataset after cleaning
print("missing value after operations")
print(df_clean.isnull().sum().sum())
df_clean.to_csv("titanic_clean.csv",index=False)

# introduce family size and isalone column
df_clean['family_size']=df_clean['sibsp']+df_clean['parch']+ 1
df_clean['is_alone']=(df_clean['family_size']==1).astype(int)
df_clean.to_csv("titanic_clean_2.csv",index=False)