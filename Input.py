import csv
import stockstats
import pandas as pd
stuff = input("Start year: ")
Startyear = int(stuff)
while (Startyear > 2020):
    print ("invalid year")
    stuff = input("Start year: ")
    Startyear = int(stuff)

stuff = input("Start month: ")
Startmonth = int(stuff)
while (Startmonth > 12) or (Startmonth < 1):
    print ("invalid month")
    stuff = input("Start month: ")
    Startmonth = int(stuff)


stuff = input("Start day: ")
startday = int(stuff)
while (startday > 31) or (startday < 1):
    print ("invalid day")
    stuff = input("Start day: ")
    startday = int(stuff)

stuff = input("End year: ")
Endyear = int(stuff)
while (Endyear > 2020) or (Endyear < 1000) or (Endyear < Startyear):
    print ("invalid Year \n")
    stuff = input("End Year: ")
    Endyear = int(stuff)

stuff = input("End month: ")
Endmonth = int(stuff)
while (Endmonth > 12) or (Endmonth < 1) or ((Endyear == Startyear) and (Endmonth < Startmonth)):
    print ("invalid month \n")
    stuff = input("End month: ")
    Endmonth = int(stuff)

stuff = input("End day: ")
Endday = int(stuff)
while (Endday > 31) or (Endday < 1) or ((Endyear == Startyear) and (Endmonth == Startmonth) and (Endday < startday)):
    print ("invalid day")
    stuff = input("End day: ")
    Endday = int(stuff)


print ("Getting data from {year}-{month}-{day}" .format(year=Startyear, month=Startmonth, day=startday))
print ("to {year}-{month}-{day}" .format(year=Endyear, month=Endmonth, day=Endday))

Location = r'GE.csv'
df = pd.read_csv(Location, header=None)
df

stock = StockDataFrame.retype(pd.read_csv('GE.csv'))
