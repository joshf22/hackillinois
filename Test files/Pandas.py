import pandas_datareader.data as web
import datetime as dt
from stockstats import StockDataFrame

start = dt.datetime(2019,2,1)
end = dt.datetime(2019,2,22)

f = web.DataReader('AAPL', 'iex',start ,end)
rows = int((f.size-5)/5)
print(rows)


big=str(rows)
text = 'volume_-'+big+'~0_min'
print (text)
print (f)
stock = StockDataFrame.retype(f)

d = (stock['kdjk_14'])
print (d)
print (d.iloc[-1])
dval = (d.iloc[-1]+d.iloc[-2]+d.iloc[-3])/3
print ("K value is : {data} \nD value is : {dboi}" .format(data=d.iloc[-1], dboi=dval))

