import pandas as pd
a=pd.read_csv("data.csv")
a.drop_duplicates(inplace=True)
print(a.to_string())

