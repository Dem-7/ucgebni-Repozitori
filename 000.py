
import pandas as pd
tt = pd.read_csv('tt.csv')
print(tt.head())
print(tt.info())
print(tt.describe())

nnd = pd.read_csv('dz.csv')
nnd.fillna(0 , inplace = True)
a = nnd.groupby('City')['Salary'].mean()
print(a)


