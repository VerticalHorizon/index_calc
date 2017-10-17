import argparse
from pandas import read_csv

parser = argparse.ArgumentParser(description='Calculate index changes.')
parser.add_argument('--startdate',
                   default=now,
                   help='Start date')
parser.add_argument('--enddate',
                   default=now-30,
                   help='End date')
parser.add_argument('-rd', '--rolldate',
                   default=30,
                   help='Rolling date in days')
parser.add_argument('-f', '--filename',
                   default='seed.csv',
                   help='CSV file name')

args = parser.parse_args()
filename = args.filename
rolldate = int(args.rolldate)

out = read_csv(filename, sep=',', skiprows=12, header=None, usecols=range(4))

print out[:rolldate]