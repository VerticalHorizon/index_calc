import argparse
from math import sqrt
from pandas import read_excel, DataFrame
from datetime import datetime, timedelta


parser = argparse.ArgumentParser(description='Calculate index changes.')

parser.add_argument('-sd', '--startdate',
                   default=datetime.strftime(datetime.now(), "%Y%m%d"),
                   help='Start date without spaces in Ymd format. Ex: 20090114 or 2009-01-14')
parser.add_argument('-ed', '--enddate',
                   default=datetime.strftime(datetime.now() - timedelta(weeks=4), "%Y%m%d"),
                   help='End date')
parser.add_argument('-rw', '--rollwindow',
                   default=30,
                   help='Rolling daily window')
parser.add_argument('-f', '--filename',
                   default='seed.csv',
                   help='CSV file name')

args = parser.parse_args()
filename = args.filename
rollwindow = int(args.rollwindow)
startdate = args.startdate
enddate = args.enddate

df = read_excel(filename, sheetname=0, header=None, skiprows=12, usecols=range(4)).set_index(0)

# sliced by date range
sliced_df = df[startdate:enddate]

pct_change = sliced_df.pct_change()
std_deviation = pct_change.std(numeric_only=True, axis=0)

print pct_change.to_string()
print pct_change.rolling(rollwindow).std(ddof=0).apply(lambda x: x*sqrt(220) ).to_string()