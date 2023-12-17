import pandas as pd

df=pd.read_csv('c:/4-DataSets/animal_category.csv')

df.shape


df_new=pd.get_dummies(df)
df_new.shape

df_new.drop(['Gender_Male','Homly_Yes'],axis=1,inplace=True)
df_new.shape #two col can removed

df_new.rename(columns={'Gender_female':'Gender','Homly_No':'Homly'})

#.................................................................

df1=pd.read_csv("c:/4-DataSets/ethnic diversity.csv")
df1.shape
df1_new=pd.get_dummies(df1)
df1.columns
df1_new.drop(['Sex_F','MaritalDesc_Widowed','State_VT','Race_Black or African American'],axis=1,inplace=True)
df1_new.shape

