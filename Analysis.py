import pandas as pd # Data Processor
import numpy as np # Linear Algebra
import matplotlib.pyplot as plt # Plotting
import seaborn as sns # Also Plotting
import os # To Access Structure of Directory

sns.set()

data = pd.read_csv('insurance.csv')
data.head()

data.shape

data.info()

data.dtypes.unique()

data.columns

# Grouping the Data
group = data.columns.to_series().groupby(data.dtypes).groups

# Now I'll create a dictionary that'll display multiple datatypes and the columns that contain them.
dct = {k.name: v for k, v in group.items()}

# Let's display some of those different attributes.
attributes_by_datatype = pd.DataFrame(list(dct.values()), index = dct.keys(), columns = ['Attr 1', 'Attr 2', 'Attr 3'])
attributes_by_datatype

#Now, it'd be good to exploit the unique values, so let's do that.
sorted(data['children'].unique())   #children
sorted(data['region'].unique())     #region
sorted(data['sex'].unique())        #sex
sorted(data['smoker'].unique())        #smoker

# Now let's start cleaning up this data.
data.isnull().any().sort_values(ascending=True)
# No need! No missing or NaaN values!

# Next step is to convert the strings into numbers.

data['sex'] = data['sex'].apply({'female':0,'male':1}.get)
data['smoker'] = data['smoker'].apply({'yes':1, 'no':0}.get)
data['region'] = data['region'].apply({'northwest':1, 'southeast':2, 'southwest':3, 'northeast':4}.get)
data.head()

data.describe().transpose() # overview of important stats.

# Now, that the data is all cleaned up and organized, I will begin to see if there is any correlation between the variables.

corr = data.corr()
plt.figure(figsize=(16, 8))
sns.heatmap(corr, annot=True, cmap = 'viridis')
plt.show()

# Based on the results of this correlation heatmap, , we can conclude that smoking is strongly correlated - in the positive direction, with premium charges and has a weaker correlation - in the positive direction of the Age and BMI of the insured individuals with premium charges.
# Now we will the correlation of the different variables with the premium in our dataset.

corr = data.corr()[['charges']].sort_values(by='charges', ascending=False)
plt.figure(figsize=(8, 12))
sns.heatmap(corr, vmin=-1, vmax=1, annot=True, cmap = 'BrBG')
plt.show()

# Based on this correlation heatmap, we can conclude that smoking is strongly correlated (positive) with premium charges, and that sex and children show very weak correlation (positive) with premium charges. And lastly, that the region variable has the very weakest correlation (positive) with premium charges.

# As a bonus, we wanted to include this graph to represent the interesting relationship between the Premium Charges, BMI and Smoking Status (Smoker / Non - Smoker).
data.plot(kind="scatter", x="age", y="charges",
    s=data["smoker"]*25, label="smoker", figsize=(14,10),
    c='bmi', cmap=plt.get_cmap("jet"), colorbar=True,
    sharex=False)
plt.legend()