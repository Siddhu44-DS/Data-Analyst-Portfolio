
### Plot Cheat Sheet

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Distribution - Histogram uses(Distribution, Skewness, Normality)
plt.figure(figsize=(5,10))
sns.hist(data=df, x='Sales', kde=True)
plt.title('title')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.xticks(rotation=90)
plt.show()

#nulls 
df.isnull()
missing_pct = (df.isnull.sum()/len(df))*100
plt.hist(df['missing_pct'])
plt.show()

# Box Plot (outliers, spread analyis)
sns.barplot(data=df, x='departmen', y='salary') #y is num and x is category wise
plt.title('Sales Box Plot')
plt.show()

# Count plot Categorical Frequency
plt.figure(figsize=(15,5))
sns.countplot(data=df, x='company', order = df['company'].value_counts().index)
plt.xticks(rotation=90)
plt.title("Comapny and no of items sold")

# Bar Plot (Category comparisions)
sns.barplot(data=df, x='departmen', y='salary')

# Line Plot (Time Series, Trend)
sns.lineplot(data=df, x='date', y='sales')

# Scatter plot(Relationship)
sns.scatterpolt(data=df, x='sales', y='profit')

# Heatmap (Multivarient analysis, features relationship)
corr=df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)

# Pairplot (Quick relationship check for all numeric columns)
sns.paorplot(df)

