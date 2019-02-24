import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from stockstats import StockDataFrame
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

start = dt.datetime(2019,2,1)
end = dt.datetime(2019,2,22)

f = web.DataReader('AAPL', 'iex',start ,end)
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

%matplotlib inline


comb["K"].plot(grid=True)
plt.show()

