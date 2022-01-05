import os
import csv

csvpath = os.path.join("PyBank","Resources","budget_data.csv")

print("Financial Analysis")
print("-------------------")


with open(csvpath) as csvfile:

#find total number of months
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        month_count = len(row)
print(month_count)


