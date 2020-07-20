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
filePath = os.path.join("Resources/election_data.csv")
electionOutput = os.path.join("Analysis/Election Results.text")

#variables
totVote = 0
candidateName = []

with open(filePath)