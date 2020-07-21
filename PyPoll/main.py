# PyPoll Script
# Objective: 1) Calculate total votes
#            2) Create a list of the Candidates
#            3) Percentage of Candidates votes (Candidate Total/ Total Votes).   
#            4) Sum of each Candidates votes.
#            5) Print Winner
#Import os and csv
import os
import csv

#File pathways
filepath = os.path.join("Resources/election_data.csv")
exportPath = os.path.join("Analysis/Election Results.txt")

#Variables
candidateTable = []
votes = 0
ballotCount = []

#Open the CSV file and establish varibale to read.
with open(filepath,newline="") as pollData:
    electionReader = csv.reader(pollData)
    #Variable skips header
    header = next(pollData)

    #Go through each row to tabulate votes and establishes index for Candidate
    for row in electionReader:
        votes = votes + 1
        candidate = row[2]

        #Tabulating candidate votes to candidateTable and populating ballotCount and candidateTable
        if candidate in candidateTable:
            candidateTotals = candidateTable.index(candidate)
            ballotCount[candidateTotals] = ballotCount[candidateTotals] + 1
        else:
            candidateTable.append(candidate)
            ballotCount.append(1)

    # Variable to establish the first portion of the export statement
    output1= (f"Election Results\n" + f"---------------------\n" + f"Total Votes: {votes}\n")
    
    #Variables for percentage of votes and empty string to hold results. 
    #electionResults is the second portion of the export statement
    percentages = []
    maxVotes = ballotCount[0]
    electionResults = ""
    maxName = 0

    #Find the percentage of votes for each candidate
    for i in range(len(candidateTable)):
        votePercentage = ballotCount[i]/votes*100
        percentages.append(votePercentage)
        Results=f"{candidateTable[i]}: {percentages[i]:.3f}% ({ballotCount[i]})\n"
        electionResults += Results
    
        #Determines Winner
        if ballotCount[i] == maxVotes:
            maxVotes = ballotCount[i]
            maxName = i
    
        # Winner Variable
        winner = candidateTable[maxName]

    # Variable to store the output for the third portion of export statement
    output2 = (f"----------------------\n" + f"winner: {winner}\n" + f"-----------------------")

    # Variable to concatonate export statement
    output = (output1 + electionResults + output2)

    #Printing output to terminal
    print(output)

    #Writing and Exporting file
    with open(exportPath, "w",) as txt_file:
        txt_file.write(output)

    # Closing csv file
    pollData.close()


