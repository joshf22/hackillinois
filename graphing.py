import numpy as np
import plotly.plotly as py              # for sending things to plotly
import plotly.tools as tls              # for mpl, config, etc.
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import stockstats as ss
import datetime as dt

#parsing
from numpy import genfromtxt
my_data = genfromtxt('hackillinois/GE.csv', delimiter=',', skip_header=1, dtype=(int,float,float,float,float,float,float))
columns_count = len(my_data[0])
GEstock = [[],[],[],[],[],[],[]]

for row, row_value in enumerate(my_data,0): 
    for column, column_value in enumerate(row_value,0):
        if column == 0:
            column_value = str(column_value)
            column_value = dt.datetime.strptime(column_value,"%Y%m%d").date()
        GEstock[column].append(column_value)
 
#calculating current k
past14uno = row-14 #past 14 days
current_closeuno = GEstock[5][row]
lowest_lowuno = min(GEstock[3][past14uno:row])
highest_highuno = max(GEstock[2][past14uno:row])

k = 100*(current_closeuno - lowest_lowuno)/(highest_highuno - lowest_lowuno)

#calculating array k
karray = []
krows = 14
while (krows<=row):
    past14 = krows-14 #past 14 days
    current_close = GEstock[5][krows]
    lowest_low = min(GEstock[3][past14:krows])
    highest_high = max(GEstock[2][past14:krows])
    kfresh = 100*(current_close - lowest_low)/(highest_high - lowest_low)
    karray.append(kfresh)
    krows = krows+1

darray = []
drows = 17
while (drows<=row):
        drowsm=drows-15
        drowsmm=drows-16
        drowsmmm=drows-17
        d = (karray[drowsm]+karray[drowsmm]+karray[drowsmmm])/3
        darray.append(d)
        drows = drows+1

#print(darray)

karray.pop(0)
karray.pop(1)
karray.pop(3)
print (karray)

#Graphing

fig, ax = plt.subplots()
ax.plot(GEstock[0][16:row], karray) 
ax.plot(GEstock[0][16:row], darray) 
plt.ylim([0,100])
ax.set(xlabel='time', ylabel='k/d', title= ("Current k =  {kay}" .format(kay=k)) )
ax.grid()

fig.savefig("test.png")
plt.show()





#printing array
#print (GEstock)

print (k)
