### this is the second model which will predict the disease based on the symptoms and test results

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from database import db_connection
from healthcare_system import df
from sklearn.model_selection import train_test_split

feature = ['age', 'gender', 'severity_score', 'test_name', 'test_result']
target = 'disease_name'

# Create separate encoders for each categorical column
le_disease = LabelEncoder()
le_gender = LabelEncoder()
le_test_name = LabelEncoder()
le_test_result = LabelEncoder()

# Encode categorical columns
df['disease_name'] = le_disease.fit_transform(df['disease_name'])
df['gender'] = le_gender.fit_transform(df['gender'])
df['test_name'] = le_test_name.fit_transform(df['test_name'])
df['test_result'] = le_test_result.fit_transform(df['test_result'])

# Use encoded features for training
X = df[['age', 'gender_encoded', 'severity_score', 'test_name_encoded', 'test_result_encoded']]
y = df['disease_name']


#Train, test and Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#Evaluating the model
print("Accuracy:", accuracy_score(y_test, y_pred))

# For classification report, we need the original string labels
y_test_original = le_disease.inverse_transform(y_test)
y_pred_original = le_disease.inverse_transform(y_pred)
print("Classification Report:\n", classification_report(y_test_original, y_pred_original))

#prediction
new_patient = pd.DataFrame({
    'name': ['James'],
    'age': [60],
    'gender': ['Male'],
    'severity_score': [3],  # Assuming high severity
    'test_name': ['Malaria Test'],  # Use exact case from training data
    'test_result': ['Positive']     # Use exact case from training data
})

# Encode categorical features using the same encoders
#new_patient['gender'] = le_gender.transform(new_patient['gender'])
#new_patient['test_name'] = le_test_name.transform(new_patient['test_name'])
#new_patient['test_result'] = le_test_result.transform(new_patient['test_result'])

# Select encoded features for prediction
new_patient_features = new_patient[['age', 'gender', 'severity_score', 'test_name', 'test_result']]

prediction = model.predict(new_patient_features)
predicted_disease = le_disease.inverse_transform(prediction)

print(f"Predicted disease: {predicted_disease[0]}")


