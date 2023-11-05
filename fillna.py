import pandas as pd
a=pd.read_csv('data.csv')
a.fillna(150,inplace=True)
print(a.to_string())
