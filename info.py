import pandas as pd
a=pd.read_csv("data.csv")
print(a.info())
print(a.info(10))