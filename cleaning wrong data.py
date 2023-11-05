import pandas as pd
a=pd.read_csv("data.csv")
a["Date"]=pd.to_datetime(a["Date"])
print(a.to_string())

'''
the date in row 26 was fixed,
but the empty date in row 22 got
a NaT (Not a Time) value, 
in other words an empty value. 
One way to deal with empty values is
simply removing the entire row.
'''


import pandas as pd 
p=pd.read_csv("data.csv")
p["Date"]=pd.to_datetime(p["Date"])
p.dropna(subset=["Date"],inplace=True)
print(p.to_string())