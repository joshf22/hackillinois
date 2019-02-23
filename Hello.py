import csv
import numpy
stuff = input("Start year: ")
startyear = int(stuff)
while (startyear > 2020):
    print ("invalid year")
    stuff = input("Start year: ")
    startyear = int(stuff)

stuff = input("Start month: ")
startmonth = int(stuff)
while (startmonth > 12) or (startmonth < 1):
    print ("invalid month")
    stuff = input("Start month: ")
    startmonth = int(stuff)


stuff = input("Start day: ")
startday = int(stuff)
while (startday > 31) or (startday < 1):
    print ("invalid day")
    stuff = input("Start day: ")
    startday = int(stuff)

stuff = input("End year: ")
Endyear = int(stuff)
while (Endyear > 2020) or (Endyear < 1000):
    print ("invalid Year \n")
    stuff = input("End Year: ")
    startday = int(stuff)

stuff = input("End month: ")
Endmonth = int(stuff)
while (endmonth > 12) or (endmonth < 1):
    print ("invalid month \n")
    stuff = input("End month: ")
    startday = int(stuff)

stuff = input("End day: ")
endday = int(stuff)
while (endday > 31) or (endday < 1):
    print ("invalid day \n")
    stuff = input("End day: ")
    startday = int(stuff)

if (startyear > 2020):
    print ("invalid year")





print ("hello world")