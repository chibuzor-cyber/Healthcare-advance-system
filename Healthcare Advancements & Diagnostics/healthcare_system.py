import pandas as pd
from database import db_connection


query = """
SELECT 
    p.patient_id,
    p.gender,
    p.date_of_birth,
    v.visit_id,
    v.visit_date,
    d.disease_name,
    d.severity,
    l.test_name,
    l.test_result
FROM patients p
JOIN visits v ON p.patient_id = v.patient_id
JOIN diagnosis d ON v.visit_id = d.visit_id
LEFT JOIN lab_results l ON v.visit_id = l.visit_id
"""
try:
    df = pd.read_sql(query, db_connection)
    print("data Loaded Succesfully")
    print(df)

except Exception as e:
    print("Error:", e)

#Data cleaning
df.isnull().sum()
df['test_result'] = df['test_result'].fillna('none')


#Removing Duplicate 
df = df.drop_duplicates()

#Fix Data Type
df["visit_date"] = pd.to_datetime(df["visit_date"])
df["date_of_birth"] = pd.to_datetime(df["date_of_birth"])

#Feature Engineering
#creating new age
df['age'] = (pd.Timestamp.now() - df['date_of_birth']).dt.days // 365

#convert severity to numeric
severity_map = {'low': 1, 'medium': 2, 'high': 3}
df['severity_score'] = df['severity'].map(severity_map)

#create Risk score
df['risk_score'] = df['age'] * df['severity_score']

#high and low risk identification
df['high_risk'] = df['risk_score'].apply(lambda x: 1 if x > 100 else 0)

#exploratory Data Analysis
# which disease is most common
df['disease_name'].value_counts()

#which symptoms/test relate to disease
pd.crosstab(df['test_name'], df['disease_name'])

#who are high-risk patients
high_risk_patients = df[df['high_risk'] == 1]

# Close the connection
db_connection.close()
print("✓ Database connection closed")