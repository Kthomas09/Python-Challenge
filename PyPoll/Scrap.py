import os
import csv

filePath = os.path.join("Resources/election_data.csv")
electionOutput = os.path.join("Analysis/Election Results.text")

#variables
candidateTable = []
votes = 0
ballotCount = []

with open(filePath, newline="") as pollData:
    electionReader = csv.reader(pollData)
    header = next(pollData)
    for row in electionReader:
        votes = votes + 1
        candidate = row[2]
        name = row[2]
        if candidate == name:
            candidateTable.append(name)
        else: 
            candidateTable.append(candidate)
        

# Exported file with bug
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
    # printTable = f"{candidateTable[count]}: {percentages[count]:.3f}% ({ballotCount[count]})"
    # Determines winner
    if ballotCount[count] > maxVotes:
        maxVotes = ballotCount[count]
        maxName = count

# Winner Variable
winner = candidateTable[maxName]
print(f"Election Results")
print(f"---------------------")
print(f"Total Votes: {votes}")
print(candidateTable), percentages, {ballotCount}")
print(f"----------------------")
print(f"winner: {winner}")
print(f"-----------------------")

# # Varable for export text
# output = (
#     f"Election Results\n"
#     f"---------------------\n"
#     f"Total Votes: {votes}\n"
#     f"{candidateTable}: {percentages[count]:.3f}% ({ballotCount[count]})\n"
#     f"----------------------\n"
#     f"winner: {winner}\n"
#     f"-----------------------"
# )
# # Writing and Exporting file
# with open(electionOutput, "w",) as txt_file:
#     txt_file.write(output)

# # Closing csv file
# pollData.close()

