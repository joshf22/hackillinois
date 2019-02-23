import csv
import numpy as np
#import matplotlib.pyplot as plt

data_path = 'GE.csv'
types = ['|U16', 'f8', 'f8', 'f8', 'f8', 'f8', 'f8']
data = np.genfromtxt(data_path, dtype=types, delimiter=',', names=True)

# arrays for each column
dates = []
opens = []
highs = []
lows = []
closes = []
adjs = []
volumes = []
for lines in data:
	dates.append(lines[0]);
	opens.append(lines[1]);
	highs.append(lines[2]);
	lows.append(lines[3]);
	closes.append(lines[4]);
	adjs.append(lines[5])
	volumes.append(lines[6])


print(dates[:10])
