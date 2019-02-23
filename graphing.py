import numpy as np
import plotly.plotly as py              # for sending things to plotly
import plotly.tools as tls              # for mpl, config, etc.
import plotly.graph_objs as go
import matplotlib.pyplot as plt

from numpy import genfromtxt
my_data = genfromtxt('hackillinois/GE.csv', delimiter=',', skip_header=1)

columns_count = len(my_data[0])
stock = [[],[],[],[],[],[],[]]


for row in my_data: 
    for column, column_value in enumerate(row,0):
        stock[column].append(column_value)

plt.plot(stock[0],stock[1],'ro')
plt.axis([20190123,20190222,9,11])
plt.show()

print (stock)

