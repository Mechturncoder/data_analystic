# %% [markdown]
# # Matplotlib

# %% [markdown]
# - Scatter: plt.scatter(df.col1, df.col2)
# - Histogram: plt.hist(df.col, bins = 20)
# - Box plot: plt.boxplot(df.col)
# - Line plot: 
#     - df_sorted = df.sort_values(by=col_name)
#     - plt.plot(df.col_name, df.col2, line_style = '--', color = 'b')
# - Bar: df.col_name.value_counts().plot(kind = 'bar')
# - Pie: df.col_name.value_counts().plot(kind = 'pie', autopct = '%1.1f%%', startangle=90)

# %% [markdown]
# Python
# 
# `import matplotlib.pyplot as plt`
# 
# `plt.figsize=(18,16) => 1800 x 1600 size of a subplot layout to accomodate different types of plot`
# 
# `plt.subplot(ncol, nrow, n: order of proirity)`
# 
# `plt.tight_layout()`
# 
# `plt.show()`

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('./data_pd/heart.csv')

# %%
# Creating a subplot layout to accomodate different types of plot
plt.figure(figsize=(18,16))

# %% [markdown]
# # Scatter Plot

# %%
plt.subplot(3,2,1)
plt.scatter(df['age'],df['chol'])
plt.title("Age vs Cholestrol")

# %% [markdown]
# # Histogram

# %%
plt.subplot(3,2,2)
plt.hist(df['trestbps'], bins=20)
plt.title('resting BP distribution')

# %% [markdown]
# # Box Plot

# %%
plt.subplot(3,2,3)
plt.boxplot(df['thalach'])
plt.title('Max heart rate')

# %% [markdown]
# # Line plot

# %%
plt.subplot(3,2,4)
df_sorted = df.sort_values(by='age')    # sort by age for line plot
plt.plot(df_sorted['age'], df_sorted['chol'], linestyle='--', color = 'b')
plt.title('Age vs Cholestrol line')


# %% [markdown]
# # Bar Plot

# %%
plt.subplot(3,2,5)
df['gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Heart Disease Target Proportion')


# %%
plt.tight_layout()
plt.show()

# %%



