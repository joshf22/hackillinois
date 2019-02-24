import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from stockstats import StockDataFrame
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

start = dt.datetime(2018,12,10)
end = dt.datetime(2019,2,22)

ticker = input("Enter a ticker: ")
year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
date1 = dt.date(year, month, day)
year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
date2 = dt.date(year, month, day)
print (ticker)

f = web.DataReader(ticker, 'iex',date1 ,date2)
rows = int((f.size-5)/5)


big=str(rows)
text = 'volume_-'+big+'~0_min'
print (f)
print("\n")
stock = StockDataFrame.retype(f)

k = (stock.get('kdjk_14'))
dval = (k.iloc[-1]+k.iloc[-2]+k.iloc[-3])/3
d = k.rolling(3,min_periods=1).mean()
comb = pd.merge(k,d, on=['date'], how='left')
print("\n")
comb.rename(columns = {'':'Date', 'kdjk_14_x':'K','kdjk_14_y':'D'}, inplace=True)
print (comb)
fig, axes = plt.subplots (nrows=2,ncols=1)
ax = comb.plot(figsize=(10 , 10),ax=axes[1], title="K and D values over the time period")
ax.set_ylabel("Value")
ax.set_ylim([0,100])
ax.patch.set_facecolor('black')
ax.patch.set_alpha(.2)

ax1 = f.plot(y="close",ax=axes[0])
ax1.patch.set_facecolor('black')
ax1.patch.set_alpha(.2)


plt.savefig("output/plot.png")





