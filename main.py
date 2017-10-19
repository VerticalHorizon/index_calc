import argparse
from math import sqrt
import pandas as pd
from datetime import datetime, timedelta


parser = argparse.ArgumentParser(description='Calculate index changes.')

# available params
parser.add_argument('-sd', '--startdate',
                   default=datetime.strftime(datetime.now() - timedelta(weeks=4), "%Y%m%d"),
                   help='Start date without spaces. Ex: 20090114 or 2009-01-14')
parser.add_argument('-ed', '--enddate',
                   default=datetime.strftime(datetime.now(), "%Y%m%d"),
                   help='End date without spaces. Ex: 20090114 or 2009-01-14')
parser.add_argument('-rw', '--rollwindow',
                   default=30,
                   help='Rolling daily window')
parser.add_argument('-f', '--filename',
                   default='seed.csv',
                   help='CSV file name')
parser.add_argument('-o', '--outfile',
                   default='out.csv',
                   help='Out CSV file name')

args = parser.parse_args()
filename = args.filename
outfile = args.outfile
rollwindow = int(args.rollwindow)
startdate = args.startdate
enddate = args.enddate

df = pd.read_csv(filename, header=None).set_index(0)

# sliced by date range
sliced_df = df[startdate:enddate]

# Percent change
pct_change = sliced_df.pct_change()
# Moving standard deviation
std_deviation = pct_change.rolling(rollwindow).std(ddof=0).apply(lambda x: x*sqrt(220) )

out = pd.concat([pct_change, std_deviation], axis=1)
out.to_csv(outfile, header=False)
