import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats



df = pd.read_csv("scosco_flow.txt")

# convert l/min to l/hour
df["CR10x_lh"] = 60 * df["CR10x"]


x = df["CR10x_lh"]
y =  df["Mechanical"]
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

plt.plot(x, y, '.')
plt.xlabel("CR10")
plt.ylabel("Mechanical")
plt.plot(x, intercept + slope*x, 'r', label=f'{slope:.2f} x + {intercept:.2f}')
plt.legend()
plt.show()

