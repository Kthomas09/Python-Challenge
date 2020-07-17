#PyPoll Python Script

#Importing CSV and OS
import csv
import os

#Poll Data Pathway
poll_data_csv = os.path.join("PyPoll/Resources/election_data.csv")

with open(poll_data_csv) as poll_data:
    reader =csv.reader(poll_data)
    header = next(poll_data)
    print (header)
    
    
    
    #Variable for Total Votes
    total_votes = 0
    #For loop to iterate through polling data to calculate total votes and reassign total votes variable.
    for row in poll_data:
        total_votes += 1



# Election Results Table
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")

