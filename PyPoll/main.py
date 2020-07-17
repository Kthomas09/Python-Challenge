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
    