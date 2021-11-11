# Uses data available at http://data.worldbank.org/indicator
# on Forest area (% of land area) and Agricultural land area (% of land area).
#
# Prompts the user for two distinct years between 1960 and 2020,
# separated by two consecutive hyphens with possibly spaces before
# and after, as well as a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area (as a ratio) has strictly increased from
#   oldest input year to most recent input year;
# - forest area (as a ratio) has strictly increased from oldest input
#   year to most recent input year;
# - the ratio of increase in agricultural land area to
#   increase in forest area (so a ratio of ratio differences)
#   determines output order.
#
# Countries are output from those whose ratio of increases is largest
# to those whose ratio of increases is smallest, as a floating point
# number with 2 digits after the decimal point.
#
# In the unlikely case where many countries share the same ratio
# of increases, countries are output in lexicographic order.
#
# In case fewer than N countries are found, only that number of
# countries is output.
#
# If no country has data for both years, then a special message is output.
#
# The data directory is stored in the working directory.


from collections import defaultdict
import csv
import os
from pathlib import Path
import sys

# INSERT YOUR CODE HERE


try:
    years = {int(year) for year in
    input('Input two distinct years in the range 1960 -- 2020: ').split('--')
 }
    if len(years) != 2 or any(year < 1960 or year > 2020 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    input_number = int(input('Input a strictly positive integer: '))
    if input_number < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()

input_year = []
input_year = sorted(years)
if input_year[0]<input_year[1]:
    formyear = input_year[0]
    backyear = input_year[1]
else:
    formyear = input_year[1]
    backyear = input_year[0]
data = defaultdict(list)
# Insert your code here
with open(Path('Areas/Agricultural Land')/r'API_AG.LND.AGRI.ZS_DS2_en_csv_v2_2056230.csv',encoding = 'utf-8') as a:
    agrc = csv.reader(a)
    for i in range(5):
        header = next(agrc)
    for row in agrc:
        if(not row):
            continue
        country_name = row[0]
        agr_formyear = row[formyear-1960+4]
        agr_backyear = row[backyear-1960+4]
        data[country_name].append(agr_formyear)
        data[country_name].append(agr_backyear)

with open(Path('Areas/Forest')/r'API_AG.LND.FRST.ZS_DS2_en_csv_v2_2125884.csv',encoding = 'utf-8') as b:
    forest = csv.reader(b)
    for i in range(5):
        header = next(forest)
    for row in forest:
        if(not row):
            continue
        country_name = row[0]
        fore_formyear = row[formyear-1960+4]
        fore_backyear = row[backyear-1960+4]
        data[country_name].append(fore_formyear)
        data[country_name].append(fore_backyear)

results = defaultdict(list)
for country in data:
    if data[country][0] != '' and data[country][1] != '' and data[country][2] != '' and data[country][3] != '':
        if float(data[country][1])-float(data[country][0]) >= 0 and float(data[country][3])-float(data[country][2]) > 0 :
            ratio = ((float(data[country][1])-float(data[country][0]))/(float(data[country][3])-float(data[country][2])))
            results[country].append(ratio)
results = sorted(results.items(), key=lambda x: x[1],reverse=True)

if len(results) == 0:
    print('I do not have data for any country for at least one of those years.')
else:
    print(f'Here are the top {input_number} countries or categories where, between {formyear} and {backyear},\n'
      '  the ratios of agricultural land area and forest area\n'
      '  (over total land) have both strictly increased,\n'
      '  listed from the countries where the ratio of increases\n'
      '  is largest, to those where it is smallest:')
    if len(results)<input_number:
        for i,j in results:
            print('{} ({:.2f})'.format(i, *j))
    elif len(results)==input_number or len(results)>input_number:
        count = 0
        for i,j in results:
            if count == input_number:
                break
            else:
                print('{} ({:.2f})'.format(i, *j))
                count = count+1

