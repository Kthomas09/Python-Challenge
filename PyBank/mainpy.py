#PyBank Python Script

#Importing CSV and OS
import csv
import os

#Budget Data Pathway
file_to_budget_data = r"/Users/kent.thomas/Repository/Python-Challenge/PyBank/Resources/budget_data.csv"

#Opening 
with open(file_to_budget_data) as budget_data:
    reader = csv.reader(budget_data)
    header = next(budget_data)

    

