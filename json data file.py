import pandas as pd
print(pd.read_json("data.json"))
b=pd.read_json("data.json")
print(b.to_string())