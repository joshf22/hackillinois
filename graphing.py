import numpy as np
import plotly.plotly as py              # for sending things to plotly
import plotly.tools as tls              # for mpl, config, etc.
import plotly.graph_objs as go
import matplotlib.pyplot as plt

import datetime as dt

from numpy import genfromtxt
my_data = genfromtxt('hackillinois/GE.csv', delimiter=',', skip_header=1, dtype=(int,float,float,float,float,float,float))
columns_count = len(my_data[0])
stock = [[],[],[],[],[],[],[]]


for row in my_data: 
    for column, column_value in enumerate(row,0):
        if column == 0:
            column_value = str(column_value)
            column_value = dt.datetime.strptime(column_value,"%Y%m%d").date()
        stock[column].append(column_value)
        

fig, ax = plt.subplots()
ax.plot(stock[0], stock[1])

ax.set(xlabel='time (s)', ylabel='Open ($)',
       title='Open $ vs Time')
ax.grid()

fig.savefig("test.png")
plt.show()

print (stock)

