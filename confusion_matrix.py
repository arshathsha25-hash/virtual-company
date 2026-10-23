import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix

#load the data set
df=pd.read_csv('titanic_clean_2.csv')

#split the features and target
x = df.drop(columns=['survived','alive'])
y = df['survived']

#getting dummies

x =pd.get_dummies(x, drop_first=True)

#train/test split
x_train,x_test,y_train,y_test=train_test_split(x , y,test_size=0.2,random_state=42)

#train random forest
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train, y_train)

#predict
y_pred=model.predict(x_test)

#evaluate
print('===confusion matrix==')
print(confusion_matrix(y_test,y_pred))

print("\n\n===Classification MAtrix ==")
print(classification_report(y_test,y_pred))