import os
import csv

csvpath = os.path.join("Pybank", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    months = []
    profit = []
    profit_change = []

    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))




month_count = len(months)
profits_total = sum(profit)
Average_change =(profits_total) / month_count



print("Financial Analysis")
print("-------------------")
print('Total Months: ' + str(month_count))
print('Total Profit: ' + str(profits_total))
print('Average Change: ' + str(Average_change))


