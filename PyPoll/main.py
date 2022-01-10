import os
import csv

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    total_votes = []
    khan = 'Khan'
    correy = 'Correy'
    li = 'Li'
    tooley = "O'Tooley"
    khan_count = 0
    correy_count = 0
    li_count = 0
    tooley_count = 0

    for row in csvreader:
        #total votes collection
        total_votes.append(row[0])
        #indivual candidate votes
        if row[2] == khan:
            khan_count += 1
        elif row[2] == correy:
            correy_count += 1
        elif row[2] == li:
            li_count += 1
        elif row[2] == tooley:
            tooley_count += 1
#count total votes
total_votes_count = len(total_votes)

#find percentages
khan_percent = round(khan_count/total_votes_count *100)
correy_percent = round(correy_count/total_votes_count *100)
li_percent = round(li_count/total_votes_count *100)
tooley_percent = round(tooley_count/total_votes_count *100)

#find winner
if khan_count > correy_count and khan_count > li_count and khan_count > tooley_count:
    winner = "Khan"
elif correy_count > khan_count and correy_count > li_count and correy_count > tooley_count:
    winner = "Correy"
elif li_count > khan_count and li_count > correy_count and li_count > tooley_count:
    winner = "Li"
elif tooley_count > khan_count and tooley > correy_count and tooley_count > li_count:
    winner = "O'Tooley"

#print results
print('Election Results')
print('-----------------')     
print('Total Votes ' + str(total_votes_count))
print('-----------------')
print('Khan: ' + str(khan_percent) + '%' + ' ' + '(' + str(khan_count) + ')')
print('Correy: ' + str(correy_percent) + '%' + ' ' + '(' + str(correy_count) + ')')
print('Li: ' + str(li_percent) + '%' + ' ' + '(' + str(li_count) + ')')
print("O'Tooley: " + str(tooley_percent) + '%' + ' ' + '(' + str(tooley_count) + ')')
print('-----------------')
print('Winner: ' + str(winner))

output_path = os.path.join("PyPoll", "Analysis", "Results.csv")

with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow('Election Results')
    csvwriter.writerow('-----------------')     
    csvwriter.writerow('Total Votes ' + str(total_votes_count))
    csvwriter.writerow('-----------------')
    csvwriter.writerow('Khan: ' + str(khan_percent) + '%' + ' ' + '(' + str(khan_count) + ')')
    csvwriter.writerow('Correy: ' + str(correy_percent) + '%' + ' ' + '(' + str(correy_count) + ')')
    csvwriter.writerow('Li: ' + str(li_percent) + '%' + ' ' + '(' + str(li_count) + ')')
    csvwriter.writerow("O'Tooley: " + str(tooley_percent) + '%' + ' ' + '(' + str(tooley_count) + ')')
    csvwriter.writerow('-----------------')
    csvwriter.writerow('Winner: ' + str(winner))