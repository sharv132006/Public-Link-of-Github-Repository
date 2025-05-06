
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Bar Plot for Survival by Pclass
grouped = pd.crosstab(data['Pclass'],data['Survived'])
grouped.plot(kind='bar',stacked=True)

plt.xlabel('Pclass')
plt.ylabel('Count')
plt.title('Survival by Pclass')
plt.legend(['Not Survived','Survived'])

plt.show()




