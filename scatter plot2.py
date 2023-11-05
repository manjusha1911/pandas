import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
a=pd.read_csv("data.csv")
a.plot(kind="scatter",x="Duration",y='Maxpulse')
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()