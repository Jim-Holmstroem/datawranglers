#!/usr/bin/python
import pandas as pd
import numpy as np
import matplotlib.pyplot as pplot

# Set number of rows to read for the file to speed up processing
# To read all rows, set this to None
ROWS_TO_READ = 2**16
df = None  # main data frame should be accessible to everyone


def load_data():
    print "loading data..."
    if ROWS_TO_READ is not None:
        print "Reading only %i rows of data" % ROWS_TO_READ
    global df
    df = pd.read_csv('data/airplane_2008.csv',
                     parse_dates={'datetime': ['Year', 'Month', 'DayofMonth']},
                     nrows=ROWS_TO_READ)
    print "Data loaded. Sample data:\n"
    df['id'] = df.index
    print df.iloc[:, 0:5].head()


def challenge1a():
    print "(1a) Starting day of week analysis..."
    print "Now pivoting data..."
    day_pivot = df.pivot(index='id', columns='DayOfWeek', values='ArrDelay')
    print "Loading graph"
    day_pivot.boxplot()
    pplot.show()

    #TODO: Show numerical answers


def challenge1b():
    print "(1b) Starting season analysis."
    # Add in a seasons column:
    # Season - Months
    # Winter (0) - Dec (12), Jan (1), Feb (2)
    # Spring (1) - Mar (3), Apr (4), May (5)
    # Summer (2) - Jun (6), Jul (7), Aug (8)
    # Autumn (3) - Sep (9), Oct (10), Nov (11)
    df['Season'] = df['datetime'].apply(lambda x: int(x.month % 12 / 3))

    # Now pivot the data
    print "Now pivoting data..."
    season_pivot = df.pivot(index='id', columns='Season', values='ArrDelay')

    # Plot the data
    print "Loading graph..."
    season_pivot.boxplot()
    pplot.show()

    #TODO: Show numerical answers

if __name__ == "__main__":
    load_data()
    challenge1a()
    challenge1b()
    print "Whoo! Calculations complete."