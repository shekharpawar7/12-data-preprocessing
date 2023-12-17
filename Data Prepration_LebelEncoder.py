import pandas as pd
from sklearn.preprocessing import LabelEncoder
labelEncoder=LabelEncoder()

df=pd.read_csv("c:/4-DataSets/ethnic diversity.csv") 
df.shape

X=df.iloc[:,0:9]
X.columns
y=df['Race']

#we have a nominal data Sex,MaritalDesc
X['Sex']=LabelEncoder().fit_transform(X['Sex'])
X['MaritalDesc']=LabelEncoder().fit_transform(X['MaritalDesc'])

#also we can perform on y
y=LabelEncoder().fit_transform(y)
y=pd.DataFrame(y)

df_new=pd.concat([X,y],axis=1)
