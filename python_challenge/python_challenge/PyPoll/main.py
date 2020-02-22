#this is a file for the python_challenge for PyPoll - main.py - Randy Dettmer

import os
import csv

#path to collect data from the resources folder - location may vary on your computer
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

with open(election_csv, 'r') as csvfile:
    
    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
  
    total_votes = 0 #establish variable to collect total votes
    candidate =[] #generate list for candidate pool
    
    header = next(csvreader) #skip header row
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidate:
            candidate.append(row[2])

vote_count = {} #open a dictionary for vote data
for totals in candidate:
    vote_count[totals] = [0,0]
    
#path to collect data from resources folder to populate the vote_count dictionary
#location may vary on your computer
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

with open(election_csv, 'r') as csvfile:
    
    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader) #skip header row
    for row in csvreader:
        for key, value in vote_count.items():
            if key == row[2]:
                value[1] = value[1] + 1 #collect number of votes for each candidate
                value[0] = round(((value[1]/total_votes)*100),1) #calculate percent of total vote to one decimal point

print("Election Results")
print("--------------------------")
print("Total Votes: ",str(total_votes))
print("--------------------------")
#print percentages and votes for all candidates that received votes
for key, value in vote_count.items():
    print(key, ': ', value)

#determine overall winner of the election
high_vote = 0
for key, value in vote_count.items():
    if value[1] > high_vote:
        high_vote = value[1]
        winner = key

print("============================")
print("The winner is: ", str(winner))
print("============================")

#specify the file to write to
output_path = os.path.join("new.csv")

#open the file using write mode
with open(output_path, 'w', newline='') as csvfile:
    #initialize csv writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    #write the first row - column headers
    csvwriter.writerow(['Total Votes:','Candidate, Percent of Vote, Total Votes','Winner'])
    #write the second row
    csvwriter.writerow([total_votes, vote_count, winner])
 