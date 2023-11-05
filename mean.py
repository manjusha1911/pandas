import pandas as pd
a=pd.read_csv("data.csv")
x=a['Calories'].mean()
a["Calories"].fillna(x,inplace=True)
print(a.to_string())