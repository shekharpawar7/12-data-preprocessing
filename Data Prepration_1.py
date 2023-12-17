
import pandas as pd
import seaborn as sns
df=pd.read_csv('c:/4-DataSets/ethnic diversity.csv')
df.head()
df.shape
df.columns
df.index
df.describe()
df.std()
df.mean()
sns.histplot(df)
sns.boxplot(df)
sns.kdeplot(df)
sns.barplot(df)
sns.scatterplot(df)

# # Datatype
df.dtypes
df.Salaries=df.Salaries.astype(int)
#convert float into int
df.dtypes
df.age=df.age.astype(float)
#convert age into float
df.dtypes

# # Data Duplicate
import pandas as pd
df1=pd.read_csv('c:/4-DataSets/education.csv')
duplicated=df1.duplicated()
sum(duplicated)
#calculate dublicate value
df2=pd.read_csv('c:/4-DataSets/mtcars.csv')
duplicated1=df2.duplicated()
sum(duplicated1)
df3=pd.read_csv('c:/4-DataSets/mtcars_dup.csv')
duplicated2=df3.duplicated()
sum(duplicated2)
df_new=df3.drop_duplicates()
#remove the duplicates in dataset

sum(df_new.duplicated())

#....................................................................................
#exercises
import pandas as pd

df1=pd.read_csv('c:/4-DataSets/Boston.csv')
df=pd.read_csv('c:/4-DataSets/OnlineRetail.csv')

sum(df1.duplicated())

#-------------------------------------------------------------------------------
#Outlier Treatment

import pandas as pd
import seaborn as sns
df=pd.read_csv('c:/4-DataSets/ethnic diversity.csv')
df.head()
sns.boxplot(df.Salaries)
#there is a outlier

sns.boxplot(df.age)
#there is no any outlier

IQR=df.Salaries.quantile(0.75) - df.Salaries.quantile(0.25)
IQR
lower_limit=df.Salaries.quantile(0.25) - 1.5 * IQR
upper_limit=df.Salaries.quantile(0.75) + 1.5 * IQR
lower_limit
upper_limit


#trimmming
import numpy as np
outlier_df=np.where(df.Salaries > upper_limit,True,np.where(df.Salaries < lower_limit ,True,False))
df_trimmed=df.loc[~outlier_df]
df.shape  #(310, 13)
df_trimmed.shape   #(306, 13)

#-------------------------------------------------------------------------------------------
#replacement technique

df=pd.read_csv('c:/4-DataSets/ethnic diversity.csv')
df.describe()
df_replace=pd.DataFrame(np.where(df.Salaries > upper_limit , upper_limit,np.where(df.Salaries < lower_limit,lower_limit,df.Salaries )))
sns.boxplot(df_replace)
