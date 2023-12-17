
#standardliztion
import pandas as pd
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()  #CREATING A OBJECT

df=pd.read_csv("c:/4-DataSets/mtcars.csv")
df1=df.iloc[:,1:]
df_new=pd.DataFrame(scalar.fit_transform(df1)) #convert array into df
res=df_new.describe()

#////////////////////////////////////////////////////////////////////////////


df2=pd.read_csv("c:/4-DataSets/Seeds_data.csv")

df_new=pd.DataFrame(scalar.fit_transform(df2))

res2=df_new.describe()


#normalization

df3=pd.read_csv("c:/4-DataSets/ethnic diversity.csv")
df3.columns

df3.drop(['Employee_Name','EmpID','Zip'],axis=1,inplace=True)

a1=df3.describe()

df3=pd.get_dummies(df3,drop_first=True)


def norm_fun(i):
    x=(i-i.min()) / (i.min() -i.max() )
    return x

df_norm = norm_fun(df3)

