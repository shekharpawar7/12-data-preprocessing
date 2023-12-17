import pandas as pd
from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()
#creting a object 

df=pd.read_csv("c:/4-DataSets/ethnic diversity.csv")

df.shape
#(310, 12)
df.columns

df=df[['Salaries','age','Position','State','Sex','MaritalDesc','Employee_Name','EmpID','Zip','CitizenDesc','EmploymentStatus','Department']]
df

df_new=pd.DataFrame(enc.fit_transform(df.iloc[:,2:]).toarray())
#we have a Salariy and age is a numeriacl that way we arrang in first and dont pass in acn

df_new.shape
#(310, 859)

