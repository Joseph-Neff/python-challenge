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

    
    
    #for profit in profits:
        #change_in_profit.append(profits[profit+1] - profits[profit])
        #change_in_profit.append(profits[profit+1] - profits[profit])
        #profits = [int(i) for i in profits]
        #change_in_profit.append = profits[i+1] - profits[i]
        #current_profit
        #profit_change.append(int(current_profit) - int(previous_profit))
        #previous_profit = 
   


#print(profits)        
month_count = len(months)
profits_total = sum(profits)
average_profit = int(sum(change_in_profit))/int(len(change_in_profit))




print("Financial Analysis")
print("-------------------")
print('Total Months: ' + str(month_count))
print('Total Profit: ' + str(profits_total))
print('Average Change: ' + str(round(average_profit)))


