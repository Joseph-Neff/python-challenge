import os
import csv

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    Total_votes = []

    for row in csvreader:
        Total_votes.append(row[0])

        