import csv

import stockstats
import pandas as pd
stuff = input("Start year: ")
while not stuff.isdigit() or 1996 > int(stuff) or int(stuff) > 2019:
    print("invalid year")
    stuff = input("Start year: ")
    continue
Startyear = int(stuff)

stuff = input("Start month: ")
while not stuff.isdigit() or 1 > int(stuff) or int(stuff) > 12:
    print("invalid month")
    stuff = input("Start month: ")
    continue
Startmonth = int(stuff)

stuff = input("Start day: ")
if Startmonth == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    while not stuff.isdigit() or 1 > int(stuff) or int(stuff) > 31:
        print("invalid day")
        stuff = input("Start day: ")
        continue
if Startmonth == 4 or 6 or 9 or 11:
    while not stuff.isdigit() or 1 > int(stuff) or int(stuff) > 30:
        print("invalid day")
        stuff = input("Start day: ")
        continue
if Startmonth == 2:
    while not stuff.isdigit() or 1 > int(stuff) or int(stuff) > 28:
        print("invalid day")
        stuff = input("Start day: ")
        continue
Startday = int(stuff)

#end
stuff = input("End year: ")
while not stuff.isdigit() or Startyear > int(stuff) or int(stuff) > 2020:
    print("invalid year")
    stuff = input("End year: ")
    continue
Endyear = int(stuff)

stuff = input("End month: ")
while not stuff.isdigit() or 1 > int(stuff) or int(stuff) > 12 or (Endyear == Startyear and int(stuff) < Startmonth):
    print("invalid month")
    stuff = input("End month: ")
    continue
Endmonth = int(stuff)

stuff = input("End day: ")
if Endmonth == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    while not stuff.isdigit() or 1 > int(stuff) or int(stuff) > 31 or (Endyear==Startyear and Endmonth==Startmonth and int(stuff) < Startday):
        print("invalid day")
        stuff = input("End day: ")
        continue
if Endmonth == 4 or 6 or 9 or 11:
    while not stuff.isdigit() or 1 > int(stuff) or int(stuff) > 30 or (Endyear==Startyear and Endmonth==Startmonth and int(stuff) < Startday):
        print("invalid day")
        stuff = input("End day: ")
        continue
if Endmonth == 2:
    while not stuff.isdigit() or 1 > int(stuff) or int(stuff) > 28 or (Endyear==Startyear and Endmonth==Startmonth and int(stuff) < Startday):
        print("invalid day")
        stuff = input("End day: ")
        continue
Endday = int(stuff)


print ("Getting data from {year}-{month}-{day}" .format(year=Startyear, month=Startmonth, day=Startday))
print ("to {year}-{month}-{day}" .format(year=Endyear, month=Endmonth, day=Endday))

Location = r'GE.csv'
df = pd.read_csv(Location, header=None)
df

stock = stockstats.StockDataFrame.retype(pd.read_csv('GE.csv'))



