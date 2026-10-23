import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

#load the data set
df=pd.read_csv("titanic_clean_2.csv")

#x and y separate features and target
x=df.drop(columns=['survived','alive'])

y=df['survived']

#one hot encoding categorical variable

x=pd.get_dummies(x,drop_first=True)
#initialize the random forest model
#n_estimation = 100 means it will build 100 descision trees
model=RandomForestClassifier(n_estimators=100,random_state=42)

#run cross 5 fld validation cv=5
scores = cross_val_score(model,x,y,cv=5)

#print the results
print('scores for each :',scores)
print(f'mean Accuracy : {scores.mean():.4f}')
print(f'standard Deviation {scores.std():.4f}')