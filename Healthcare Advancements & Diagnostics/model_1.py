### This is the first model which will predict the risk level of a patient based on their age and severity score

import pandas as pd
from database import db_connection
from healthcare_system import df
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score, classification_report
#Feature engineering

feature = ['age', 'severity_score']
target = 'high_risk'

X = df[feature]
y = df[target]

#Training and testing model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#Evaluating the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

#prediction 
new_Patient = [[60, 1]] #Age and Severity Score
prediction = model.predict(new_Patient)

if prediction == 1:
    print("the Patient is at high risk")
else:
    print("the Patient is at low risk")