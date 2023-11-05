import sys
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv("data.csv")
a.plot(kind='scatter',x='Duration',y='Calories')
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()