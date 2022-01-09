import os
import csv

csvpath = os.path.join("PyBank","Resources","budget_data.csv")

print("Financial Analysis")
print("-------------------")


with open(csvpath) as csvfile:

#find total number of months
    csvreader = csv.reader(csvfile, delimiter=",")
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    print(csvreader)

    for months in csvreader:
        month_count = len(months)

print(month_count)


