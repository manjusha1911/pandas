import pandas as pd
a=[1,7,2]
a=pd.Series(a)
print(a[0])
# 1

print(pd.Series(a[0]))

'''
0    1
dtype: int64
'''