import pandas as pd
import numpy as np
df=pd.read_csv("c:/4-DataSets/modified ethnic.csv")
df.isna().sum()
""" Position            43
    State               35
    Sex                 34
    MaritalDesc         29
    CitizenDesc         27
    EmploymentStatus    32
    Department          18
    Salaries            32
    age                 35
    Race                25
    dtype: int64"""
    
from sklearn.impute import SimpleImputer
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
df['Salaries']=pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))
df['Salaries'].isna().sum()   #------0

