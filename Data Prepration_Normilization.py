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
