import os
import csv

csvpath = os.path.join("PyBank","Resources","budget_data.csv")

print("Financial Analysis")
print("-------------------")

with open(csvpath) as csvfile:

#find total number of months
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    months = []
    profits = []
    profit_change = []
    
    for row in csvfile:
        months.append(row[0])
        profits.append(row[1])
    
    
    month_count = len(months)
    profits = [int(item) for item in profits]
    profits_total = sum(profits)

print('Total Months: ' + str(month_count))
print('Total Profit: ' + str(profits_total))






