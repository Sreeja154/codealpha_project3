import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Name': ['Amit', 'Sita', 'John', 'Priya', 'Raj', 'Sara', 'Kiran', 'Maya', 'Arjun', 'Neha'],
    'Department': ['CSE', 'ECE', 'MECH', 'CSE', 'ECE', 'CIVIL', 'MECH', 'CSE', 'CIVIL', 'ECE'],
    'Age': [18, 19, 18, 20, 19, 21, 20, 18, 21, 19],
    'Grade': [85, 78, 92, 88, 74, 80, 83, 90, 75, 79]
}


df = pd.DataFrame(data)

print("=== New Students Details ===")
print(df)

plt.figure(figsize=(8, 5))
sns.countplot(x='Department', data=df, palette='Set2')
plt.title('Number of Students per Department')
plt.xlabel('Department')
plt.ylabel('Number of Students')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=4, kde=True, color='skyblue')
plt.title('Age Distribution of New Students')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Department', y='Grade', data=df, palette='pastel')
plt.title('Grade Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Grade')
plt.show()

avg_grades = df.groupby('Department')['Grade'].mean().reset_index()
print("\n=== Average Grade per Department ===")
print(avg_grades)