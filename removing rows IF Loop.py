import pandas as pd
a=pd.read_csv("data.csv")
for i in a.index:
    if a.loc[i,"Duration"]>120:
        a.loc[i,"Duration"]=120
print(a.to_string())




import pandas as pd
a=pd.read_csv("data.csv")
for i in a.index:
    if a.loc[i,"Duration"]>120:
        a.drop(i,inplace=True)
    print(a.to_string())