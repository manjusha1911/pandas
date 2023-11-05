import pandas as pd
a=pd.read_csv("data.csv")
# x=a["Calories"].mode()[0]
x=a["Calories"].mode()
a["Calories"].fillna(x,inplace=True)
print(a.to_string())