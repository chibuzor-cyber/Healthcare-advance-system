from healthcare_system import df
import matplotlib.pyplot as plt
import seaborn as sns

#diease distribution
#df['disease_name'].value_counts().plot(kind='bar', color='red')
#plt.bar(df['disease_name'].value_counts().index, df['disease_name'].value_counts().values, color='red')
#plt.title("disease Distribution")
#plt.show()

#Age vs Risk_Score
#plt.plot(df['age'], df['risk_score'], color='blue')
#plt.xlabel('Age')
#plt.ylabel('Risk_Score')
#plt.title('age vs Risk_Score')
#plt.show()

#severity distribution
#df['severity'].value_counts().plot(kind='pie', autopct='%1.1f%%')
#plt.title("Severity Distribution")
#plt.show()

#Disease ditribution for seaborn
sns.countplot(data=df, x='disease_name')
plt.title("Disease Distribution")
plt.xticks(rotation=45)
plt.show()

sns.scatterplot(data=df, x='age', y='risk_score', hue='high_risk')
plt.title("Age vs Risk Score")
plt.show()

sns.countplot(data=df, x='severity')
plt.title("Severity Levels")
plt.show()

sns.boxplot(data=df, x='severity', y='age')
plt.title("Age Distribution by Severity")
plt.show()