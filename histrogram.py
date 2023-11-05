import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use("Agg")
a=pd.read_csv("data.csv")
a["Duration"].plot(kind="hist")
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()