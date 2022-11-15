#Create a Python script that analyzes the PyBank records to calculate the result

#Import dependencies
import os
import csv

# collect data from the Resources
file = os.path.join("resources", "election_data.csv")
# Create an Empty file for Poll
poll = {}

#Define Variables
total_votes = 0

#Open and read the data from the CSV file
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    next(csvread, None)

    #counts votes for each candidate as entries
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
   #Define Variables
candidate = []
votes = []

#Set Values for candidates and votes
for key, value in poll.items():
    candidate.append(key)
    votes.append(value)

# creates vote percent list
percentage_vote = []
for n in votes:
    percentage_vote.append(round(n/total_votes*100, 1))

# zips candidates, votes, percentage_vote into tuples
clean_data = list(zip(candidate, votes, percentage_vote))

#creates win_list to put winners
win_list = []

for name in clean_data:
    if max(votes) == name[1]:
        win_list.append(name[0])

# makes win_list a str with the first entry
winner = win_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(win_list) > 1:
    for w in range(1, len(win_list)):
        winner = winner + ", " + win_list[w]

#prints to file
output_file = os.path.join("analysis", "election_results.txt")

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())

