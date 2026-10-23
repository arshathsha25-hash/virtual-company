import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#load the dataset

df=pd.read_csv("titanic_clean.csv")

#remove column survived alive to avoid data leakage
#separate target and features

x = df.drop(columns=['survived','alive'])
y = df['survived']

#one hot encoding
x=pd.get_dummies(x,drop_first=True)

#split train teast split to 80% at random 42
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#train the model logistic regression
model=LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

#predict the model

y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)

#result
print(f"baseline model prediction : {accuracy:.6f}")

print("==="*5)

