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
    Total_Months = 0
    Total_Net_Profit = 0
    for row in reader: 
        Total_Months+=1
        Total_Net_Profit = Total_Net_Profit + int(row[1])

#Printing Financial Analysis Table
    print("Fiancial Analysis")
    print("-----------------")
    print("Total Months: " + str(Total_Months))
    print("Total: " + str(Total_Net_Profit))

   




    

