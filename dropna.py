# removing empty cells
import pandas as pd
a=pd.read_csv("data.csv")
b=a.dropna()
print(b.to_string())

'''
Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

'''