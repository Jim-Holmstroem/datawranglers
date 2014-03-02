#!/usr/bin/python
import pandas as pd
import numpy as np
import matplotlib.pyplot as pplot

print "loading data..."

df = pd.read_csv('data/airplane_2008.csv',parse_dates={'datetime':['Year','Month','DayofMonth']})


df['id'] = df.index
print df.iloc[:,0:5].head()

print "loading graph"

x = df.pivot(index='id',columns='DayOfWeek', values='ArrDelay')
x.boxplot()
pplot.show()
