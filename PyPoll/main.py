# PyPoll Script
# Objective: 1) Calculate total votes
#            2) Create a list of the Candidates
#            3) Percentage of Candidates votes (Candidate Total/ Total Votes).   
#            4) Sum of each Candidates votes.
#            5) Print Winner
#import os and csv
import os
import csv

# file pathways
filepath = os.path.join("Resources/election_data.csv")
exportpath = os.path.join("Analysis/Election Results.txt")

# Variables
candidateTable = []
votes = 0
ballotCount = []

#open the CSV file and establish varibale to read.
with open(filepath,newline="") as polldata:
    electionReader = csv.reader(polldata)
    # variable skips header
    header = next(polldata)

    #go through each row to tabulate votes
    for row in electionReader:
        votes = votes + 1
        candidate = row[2]

        #tabulating candidate votes to candidateTable
        if candidate in candidateTable:
            candidateTotals = candidateTable.index(candidate)
            ballotCount[candidateTotals] = ballotCount[candidateTotals] + 1
        else:
            candidateTable.append(candidate)
            ballotCount.append(1)

    # ==============================================================================
    #Variables for percentage of votes
    percentages = []
    maxVotes = ballotCount[0]
    maxName = 0
    #Find the percentage of votes for each candidate
    for i in range(len(candidateTable)):
        votePercentage = round(ballotCount[i]/votes*100)
        percentages.append(votePercentage)
        # print(f"{candidateTable[i]}: {percentages[i]:.3f}% ({ballotCount[i]})")
    # # print(percentages)
    # # for count in candidateTable:
    # #     print(f"{candidateTable[count]}: {percentages[count]:.3f}% ({ballotCount[count]})")
    #     # Determines winner
        if ballotCount[i] == maxVotes:
            maxVotes = ballotCount[i]
            maxName = i
        

        # # # # Winner Variable
        winner = candidateTable[maxName]

        print(f"Election Results")
        print(f"---------------------")
        print(f"Total Votes: {votes}")
        print(f"{candidateTable[i]}: {percentages[i]:.3f}% ({ballotCount[i]}")
        print(f"----------------------")
        print(f"Winner: {winner}")
        print(f"-----------------------")

    #         # Varable for export text
    #     output = (
    #         f"Election Results\n"
    #         f"---------------------\n"
    #         f"Total Votes: {votes}\n"
    #         f"{electionResults})\n"
    #         f"{electionResults})\n"
    #         f"{electionResults})\n"
    #         f"{electionResults})\n"
    #         f"----------------------\n"
    #         f"winner: {winner}\n"
    #         f"-----------------------"
    #     )
    #         # Writing and Exporting file
    #     with open(exportpath, "w",) as txt_file:
    #         txt_file.write(output)

    #     # Closing csv file
    #     polldata.close()


