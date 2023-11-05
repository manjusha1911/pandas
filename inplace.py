'''
If you want to change the original DataFrame, use the inplace = True argument:
'''
import pandas as pd
a=pd.read_csv("data.csv")
a.dropna(inplace=True)
print(a.to_string())