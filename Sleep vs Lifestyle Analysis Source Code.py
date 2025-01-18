import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data then display first twenty columns 
data = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
data.head(20)

#Clean data
print(data.isnull().sum())
data = data.drop_duplicates()

data = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
# Replace NaN (or missing values) with "None" using the .replace() method
data.replace(to_replace=np.nan, value="None", inplace=True)

# Save changes
data.to_csv('Sleep_health_and_lifestyle_dataset.csv', index=False)
print("NaN values have been replaced with 'None'.")

# Display the first twenty columns of cleaned data
data.head(20)

# Bar graph for sleep duration vs occupation
avg_sleep_by_occupation = data.groupby('Occupation')['Sleep Duration'].mean().sort_values()
avg_sleep_by_occupation.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Sleep Duration vs Occupation (Fig 1.)', fontsize=12)
plt.xlabel('Occupation', fontsize=12)
plt.ylabel('Average Sleep Duration (hours)', fontsize=12)
plt.show()

# Bar graph for stress level vs occupation 
avg_stress_by_occupation = data.groupby('Occupation')['Stress Level'].mean().sort_values()
avg_stress_by_occupation.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Average Stress Level vs Occupation (Fig 2.)', fontsize=12)
plt.xlabel('Occupation', fontsize=12)
plt.ylabel('Average Stress Level', fontsize=12)
plt.show()

# Bar graph for stress level vs physical activity level
avg_stress_by_activity = data.groupby('Physical Activity Level')['Stress Level'].mean()
avg_stress_by_activity.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Average Stress Level vs Physical Activity Level (Fig 3.)', fontsize=12)
plt.xlabel('Physical Activity Level', fontsize=12)
plt.ylabel('Average Stress Level', fontsize=12)
plt.show()

# Scatter plot for stress level vs sleep duration 
sns.scatterplot(data=data, x='Stress Level', y='Sleep Duration', color='dodgerblue', alpha=0.8)
plt.title('Stress Level vs Sleep Duration (Fig 4)', fontsize=12)
plt.xlabel('Stress Level', fontsize=12)
plt.ylabel('Sleep Duration (hours)', fontsize=12)
plt.show()

# Bar graph for sleep quality vs stress level
sns.barplot(
    data=data,
    x='Stress Level',
    y='Quality of Sleep',
    errorbar=None,  
    hue='Stress Level',  
    palette='Blues', 
)
plt.title('Average Sleep Quality vs Stress Level (Fig 5.)', fontsize=12)
plt.xlabel('Stress Level', fontsize=12)
plt.ylabel('Average Sleep Quality', fontsize=12)
plt.show()


# Boxplot for sleep quality vs physical acitivty 
sns.boxplot(data=data, x='Physical Activity Level', y='Quality of Sleep')
plt.title('Sleep Quality vs Physical Activity Level (Fig 6.)', fontsize=12)
plt.xlabel('Physical Activity Level (Exercise)', fontsize=12)
plt.ylabel('Quality of Sleep', fontsize=12)
plt.show()

# Boxplot for sleep duration vs physical acitivity level 
sns.boxplot(data=data, x='Physical Activity Level', y='Sleep Duration')
plt.title('Sleep Duration vs Physical Activity Level (Fig 7.)', fontsize=12)
plt.xlabel('Physical Activity Level (Exercise)', fontsize=12)
plt.ylabel('Sleep Duration (hours)', fontsize=12)
plt.show()


stats = data.describe()  
print(stats)

