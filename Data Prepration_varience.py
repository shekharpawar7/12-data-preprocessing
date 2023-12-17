#varience
import pandas as pd
#chack the veriense is not equal to 0 it all ways grether than 0
df=pd.read_csv("c:/4-DataSets/ethnic diversity.csv")
df.var()
#here empid and zip is normal data
#salary has 4.441953e+08 is 4441953000 which is not close to 0

df.var()==0

df.var(axis=0)==0


#missing values
df=pd.read_csv("c:/4-DataSets/modified ethnic.csv")
