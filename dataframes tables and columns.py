import pandas as pd
a={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
print(pd.DataFrame(a))
'''
   calories  duration
0       420        50
1       380        40
2       390        45
'''


b=pd.DataFrame(a,index=["day1","day2","day3"])
print(b)
'''
      calories  duration
day1       420        50
day2       380        40
day3       390        45
'''

print(b.loc["day1"])

'''
calories    420
duration     50
Name: day1, dtype: int64
'''
