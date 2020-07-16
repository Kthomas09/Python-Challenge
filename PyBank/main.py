#PyBank Python Script

#Importing CSV and OS
import csv
import os


#Budget Data Pathway
budget_data_csv =  os.path.join("PyBank/Resources/budget_data.csv")

#Opening 
with open(budget_data_csv) as budget_data:
    reader = csv.reader(budget_data)
    header = next(budget_data)
    print(header)
    for row in reader: 
        print(row)




    

