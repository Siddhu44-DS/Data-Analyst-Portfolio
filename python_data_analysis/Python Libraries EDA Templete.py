"""
This is templete for Data Cleaning and Analysis, basically for Exploratory Data Analysis
"""

# Load Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import skew

# Load Data
df1 = pd.read_csv("c:'/path/file.csv")
df1 = pd.read_excel("c:'/path/file.csv")

#df copy for clean
df = df1.copy()

df.head()
df.tail()
df.shape()
df.columns

# Data Types
df.dtypes
df.info()

# Rename column name
df.rename(columns={'oldcolname':'newcolname'}, inplace=True)

# Sort values
df.sort_values('col', ascending=True)

# Change Dtypes
# df['col'].astype(int) returns a new series so assign reslut back
df['col'] = df['col'].astype(int)
df['col'] = df['col'].astype(float)
df['col'] = df['col'].astype(str)

# Change for multiple columns
df = df.astype({'col1':'int64', 'col2':'str', 'col3':'float64'})

# astype() performs direct type conversion and fails if values are invalid. 
# pd.to_numeric() is more flexible and can safely handle bad values using errors='coerce'. 
# For categorical columns with repeated values, astype('category') is preferred because it reduces memory usage and can improve performance.
df['col'] = df['col'].astype('category')
df['col'] = pd.to_numeric(df['col'], errors='coerce')  #Coerce handles string in num and replaces with nan

# Date
df['date'] = pd.to_datetime(df['date'])

# Satistical Summary
df.describe()
df.describe().all  #Includes Objects
df.describe(include='object')

# Missing values
df.isnull().sum()
missing_pct = (df.isnull.sum()/len(df))*100
plt.hist(df['missing_pct'])
plt.show()

# Drop Misisng values Columns if its more than >30% if not required, >50% drop for sure
# <5% safe to impute, 5-30% analyse carefully impute with advance KNN, or predictive modeling 
df.drop(columns=['col1'], inplace=True)  #Single Column modifying same df then innplace = true
df.drop(columns=['col1', 'col2'], inplace=True) #Multiple Column modifying same df then innplace = true

# Drop all Rows with na
df.dropna()

# Fill Null, 
# Mean when Data is normally distributed
# Median when outlier exists and you dont remopve
# Mode for Catogery variabels
df['col'].fillna(df['col'].mean(), inplace = True)
df['col'].fillna(df['col'].median(), inplace = True)
df['col'].fillna(df['col'].mode(), inplace = True)

# For Time Series Analyis or forcasting
df['col'].interpolate()
df['col'].fillna(method='ffill') #Fills same value from above row
df['col'].fillna(method='bfill') #Fills same value from below row

# Duplicates Check
df.duplicated().sum()
df.drop_duplicates(inplace=True)

# Unique Values for categorical variables
df['col'].unique() #Shows unique values
df['col'].nunique()  #Count of Unique values
df['col'].value_count() #Frequency count of each category

# Outlier Detection sns Box Plot

plt.figure(figsize=(8,5)
sns.boxplot(y=df['col'], x=df['col2']) #y is num and x is category wise
plt.title('Sales Box Plot')
plt.show()

# for multiple Catogories box plot in loop 
for col in ['seller_type', 'fuel_type', 'seats']:
    plt.figure(figsize=(10,5))
    sns.boxplot(y='selling_price', x=col, data=df)
    plt.title('col vs selling_price')
    plt.show()

# Find out outlier using pandas

Q1 = df['sales'].quantile(0.25)
Q3 = df['sales'].quantile(0.75)
IQR = Q3-Q1
lower_bound = Q1-(1.5*IQR)
upper_bound = Q3+(1.5*IQR)

#Outliers df
outliers = df[(df['sales']<lower_bound) & (df['sales']>upper_bound)]
outliers_pct = (len(outliers)/len(df))*100

#new df without outliers
df_clean = df[(df['sales']>= lower_bound) & df['sales']<=upper_bound] 
len(df_clean)
df_clean.shape(0)

# Check Skewness, zero or near to zero normal, Positive right skewed, Negative left skewed
df['numcol'].skew()


###### Univarient Analysis
# Numerical (Mean, Median, Distibution, outliers, skewness)
df['numcol'].describe()
sns.histplot(df['numcol'], bin=50)   #Distribution
sns.boxplot(y=df['numcol'])

# Categorical (Unique Values, Frequency)
df['catcal'].value_counts()
sns.countplot(data=df, x='catcol')

#Example of Countplot
plt.figure(figsize=(15,5))
sns.countplot(x='company', data=df, order = df['company'].value_counts().index)
plt.xticks(rotation=90)
plt.title("Comapny and no of items sold")

###### Bivarient Analysis Purpose is to find relationship
# Numerical vs Numerical
sns.scatterpolt(data=df, x='sales', y='prodit')
df[['sales','profit']].corr()

# Numerical vs Categorical
sns.boxplot(data=df, x='catcol', y='numcol')

# Categorical vs Categorical
pd.crosstab(df['catcol1'], df['catcol2'])

###### Multivarient analysis to find deeper patterns
#sales vs profit by region
sns.scatterplot(data=df, x='sales', y='profit',hue='region')
corr= df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)

# Pivot Table
pd.pivot_table(df, values='sales', index='region', columns='department', aggfunc='sum')


##### Time Series Analysis for Trend analysis
df['date']=pd.to_datetime(df['date'])
df['month']=df['date'].dt.month  #extract month

sns.lineplot(data=df, x='date', y='sales')

#### Feature Engineering (New Features to Data likie KPI, Calculations , metrics etc)
df['profit_pct']=(df['profit']/df['sales'])*100
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['quarter'] = df['date'].dt.quarter
df['weekday'] = df['date'].dt.day_name()

#Create bins
df['age_group']=pd.cut(df['age'], bins=[0,18,35,60,100], labels=['children', 'young', 'Adult', 'Senior'])
# bin tajkes as range 0-18 children, 18-35 young like this

#Equal size quantile bins
df['quantiles']=pd.qcut(df['sales'], q=4, labels=['q1','q2','q3','q4'])

#Business Analysis or Questions
df.groupby('customer')['sales'].sumn()
df.groupby('region')[['profit', 'sales']].agg(['mean', 'sum', 'max']) #Multiple agg

avg_order_value = (df['sales'].sum()/ df['order_id'].nunique())
profit_margin = (df['profit'].sum()/ df['sales'].sum()) * 100


### Other Pandas Functions

#loc label based selection
# Selecxt Salary column for row index 5
df.loc[5, 'salary']

#iloc position based
df.iloc[0,1] #first row and second column
df.iloc[:5] #First 5 rows

#Sort values by column
df.sort_vlaues(by='sales',ascending=False)

#After filtering or group by use reset index
df.reset_index(drop=True, inplace=true)

#Set index as column
df.set_index('emp_id', inplace=True)

df=pd.merge(df1, df2, on='id', how='left')  #Join left, right, inner, outer
pd.concat([df1,df2], axis=0) #concat rows
pd.concat([df1,df2], axis=1)

# Pivoting avg salary by department and gender
pd.pivot_trable(df, values='salary', index='department', columns='gender', aggfunc='mean')

# Melt (wide to Long formate)
#Example we have cols = Product, Jan, Feb and output Product, Month, Sales
pd.melt(df, id_vars='product', var_name='month', value_name='sales')

#map replace values
df['gender'] = df['gender'].map({'M':'Male', 'F':'Female'})

##Case when question
def salary_band(salary):
        if salary<30000:
            return 'low'
        elif salary>30000 & salary<60000:
            return 'medium'
        else:
             return 'high'

df['salary_band']=df['salary'].appaly(salary_band)