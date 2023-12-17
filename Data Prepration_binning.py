import pandas as pd

data=pd.read_csv("c:/4-DataSets/ethnic diversity.csv")
data.head()
data.info()


data['Salaries_new']=pd.cut(data['Salaries'], bins=[min(data.Salaries),data.Salaries.mean(),max(data.Salaries)],labels=['low','high'])


data['Salaries_new1']=pd.cut(data['Salaries'], bins=(min(data.Salaries),data.Salaries.quantile(0.25),data.Salaries.mean(),data.Salaries.quantile(0.75),max(data.Salaries)),labels=['grp1','grp2','grp3','grp4'])
