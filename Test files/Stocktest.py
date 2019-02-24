import stockstats
import pandas as pd
import numpy as np
from stockstats import StockDataFrame as Sdf
from numpy import genfromtxt


mydata = pd.read_csv('../GE.csv')
stock = Sdf.retype(mydata)
print (stock.get('pdi'))



