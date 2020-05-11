# import pandas as pd
# file = 'market_trend_copy.csv'
# df = pd.read_csv(file, sep = ',')
# print(df.head())
# # print(df.index.columns())


import csv 
import numpy as np
import matplotlib.pylab as plt
import pandas

def getColumn (file, column):
    results = csv.reader(open(file), dialect='excel')
    return (result[column] for result in results)

time = getColumn ('marketTrendInIST.csv', 0)
time[1:]
indices = getColumn(file='marketTrendInIST.csv', 3)
indices = list(map (int [1:]))
print(indices)