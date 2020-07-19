# PyPoll Script
# Objective: 1) Calculate total votes
#            2) Create a list of the Candidates
#            3) Percentage of Candidates votes (Candidate Total/ Total Votes).   
#            4) Sum of each Candidates votes.
#            5) Print Winner
#import os and csv
import os
import csv

#set input and output pathways
filePath = os.path.join("PyPoll/Resources/election_data.csv")
exportPath = os.path.join("Scrap/Analysis.text")

#variables
candidateTable = []
votes = 0
ballotCount = []

#open the CSV file and establish varibale to read.
with open(filePath,newline="") as pollData:
    electionReader = csv.reader(pollData)
    # variable skips header
    header = next(pollData)
    #go through each row to tabulate votes
    for row in electionReader:
        #Sum total votes
        votes = votes + 1
        # variable establishing Candidate index
        candidate = row[2]

        #tabulating candidate votes to candidateTable
        if candidate in candidateTable:
            candidateTotals = candidateTable.index(candidate)
            ballotCount[candidateTotals] = ballotCount[candidateTotals] + 1
        #else append 1 vote to candidate and add a new row to lists
        else:
            candidateTable.append(candidate)
            ballotCount.append(1)

#Variables for percentage of votes
percentages = []
maxVotes = ballotCount[0]
maxName = 0

#Find the percentage of votes for each candidate
for count in range(len(candidateTable)):
    votePercentage = ballotCount[count]/votes*100
    percentages.append(votePercentage)
    # Determines winner
    if ballotCount[count] > maxVotes:
        maxVotes = ballotCount[count]
        maxName = count
# Winner Variable
winner = candidateTable[maxName]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
for count in range(len(candidateTable)):
    print(f"{candidateTable[count]}: {percentages[count]}% ({ballotCount[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")