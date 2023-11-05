import pandas as pd
a=pd.read_csv("data.csv")
a["Calories"].fillna(130,inplace=True)
print(a.to_string())