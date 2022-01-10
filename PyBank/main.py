import os
import csv

csvpath = os.path.join("Pybank", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    months = []
    profits = []
    change_in_profit = []
    average_profit = 0


    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))
    
    for i in range(1, len(profits)):
        change_in_profit.append((int(profits[i]) - int(profits[i-1])))

month_count = len(months)
profits_total = sum(profits)
average_profit = int(sum(change_in_profit))/int(len(change_in_profit))
max_change = max(change_in_profit)
min_change = min(change_in_profit)

print("Financial Analysis")
print("-------------------")
print('Total Months: ' + str(month_count))
print('Total Profit: ' + "$" + str(profits_total))
print('Average Change: ' "$" + str(round(average_profit)))
print("Greatest Profit Increase: " + str(months[change_in_profit.index(max(change_in_profit))+1]) + " " + "$" + str(max_change))
print("Greatest Profit Decrease: " + str(months[change_in_profit.index(min(change_in_profit))+1]) + " " + "$" + str(min_change))

output_path = os.path.join("PyBank", "Analysis", "Results.txt")

with open(output_path, 'w') as txt_file:
    txt_file.write(f"""
    Financial Analysis
    -----------------    
    Total Months: {str(month_count)}
    Total Profit: ${str(profits_total)}
    Average Change: ${str(round(average_profit))}
    Greatest Profit Increase: {(months[change_in_profit.index(max(change_in_profit))+1])} ${str(max_change)}
    Greatest Profit Decrease: {str(months[change_in_profit.index(min(change_in_profit))+1])} ${str(min_change)}
    """)