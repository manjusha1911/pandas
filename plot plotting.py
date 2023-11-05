import pandas as pd
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

a=pd.read_csv("data.csv")
a.plot()
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()