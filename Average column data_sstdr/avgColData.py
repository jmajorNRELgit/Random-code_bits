import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('file_25 degrees_2017-07-18 14-15-15.lwi.csv', skiprows = 3, header = None)

averages = pd.DataFrame(df.mean())

#You can transpose the data by usting the .T operator

tData = averages.T

print(tData)

plt.plot(averages)
plt.show()