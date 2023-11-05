import pandas as pd
a={"name":"manjusha","age":10,"place":"Bangalore"}
print(pd.Series(a))

calories={"day1":420,"day2":380,"day3":390}
print(pd.Series(calories,index=["day1","day2"]))