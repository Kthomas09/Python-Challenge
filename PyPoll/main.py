#PyPoll Python Script

#Importing CSV and OS
import os
import csv 

#Poll Data Pathway
poll_data_csv = os.path.join("PyPoll/Resources/election_data.csv")

with open(poll_data_csv) as poll_data:
    poll_reader =csv.reader(poll_data)
    header = next(poll_data)
    # print (header)

    #Variable for Total Votes
    total_votes = 0
    candidate_total = {}
    #Function to tabulate the votes
    def poll_tabulation (poll_data):
        
    #For loop to iterate through polling data to calculate total votes and reassign total votes variable.
        for row in poll_reader:
            total_votes += 1

        for row in poll_reader:
            name = poll_reader(row[2])
            candidate_name.append(name)
        print (candidate_name)
            


# # Election Results Table
# print("Election Results")
# print("---------------------------")
# print(f"Total Votes: {total_votes}")
# print("---------------------------")

