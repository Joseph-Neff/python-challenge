import os
import csv

csvpath = os.path.join("Pybank", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    months = []
    profits = []
    profit_change = []
    current_profit = 0 
    previous_profit = 0

    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))
        current_profit = row[1]
        profit_change.append = int(current_profit) - int(previous_profit)
        previous_profit = row[1]
        
month_count = len(months)
profits_total = sum(profits)
#Average_change




print("Financial Analysis")
print("-------------------")
print('Total Months: ' + str(month_count))
print('Total Profit: ' + str(profits_total))
#print('Average Change: ' + str(Average_change))


