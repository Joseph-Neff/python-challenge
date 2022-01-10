import os
import csv
from typing import ItemsView

csvpath = os.path.join("PyBank","Resources","budget_data.csv")

print("Financial Analysis")
print("-------------------")

with open(csvpath) as csvfile:

#find total number of months
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    months = []
    profit = []
    #profit = 0
    profit_change = []
    #profit = [int(item) for item in profit]
    
    for row in csvreader:
        months.append(row[0])
        profit.append =(int(row[1]))

month_count = len(months)
profits_total = sum(profit)
    

print('Total Months: ' + str(month_count))
print('Total Profit: ' + str(profits_total))






