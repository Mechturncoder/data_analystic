""" # %%
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# %%
plt.figure(figsize=(16,14))

# %%
df = pd.read_csv('./data_pd/heart.csv')

# %%
plt.subplot(3,3,2)
sns.histplot(df['trestbps'], kde=True, color='blue')
plt.title('Resting BP distribution')

# %%
## Box Plot
plt.subplot(3,3,4)
sns.boxplot(data=df, y = 'thalach', x = 'target', palette='Set2')
plt.title('Max Heart Rate by Target')

# %%
# Line plot
plt.subplot(3,3,4)
sns.lineplot(data=df, x='age', y='chol', color='orange')
plt.title('Line plot')

# %%
plt.subplot(3,3,1)
df['gender_mod'] = df['gender'].map({0: 'Female', 1: 'Male'})
sns.scatterplot(data=df, x='age',y='chol',hue='gender_mod', alpha=0.7)
plt.title('Age vs Cholestrol')

# %%
# Bar plot (Improved count plot for 'cp' feature)
plt.subplot(3,3,5)
sns.countplot(data=df, x='cp', palette='Set1', hue='target')
plt.title('Chest pain type distribution by Target')

# %%
# Heatmap(correlation matrix)
plt.subplot(3,3,6)
relevant_columns = ['age','chol','thalach','trestbps','oldpeak','target']
correlation_matrix = df[relevant_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='0.2f', square=True, linewidths=0.5)
plt.title('Heat map of selected variables')

# %%



 """