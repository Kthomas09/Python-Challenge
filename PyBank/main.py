#PyBank Python Script

#Importing CSV and OS
import csv
import os


#Budget Data Pathway
budget_data_csv =  os.path.join("PyBank/Resources/budget_data.csv")

 # Variables for Total Months and Total Net Profit
Total_Months = 0
Total_Net_Profit = 0
Greatest_Increase = 0
Greatest_Decrease = 0

#Opening 
with open(budget_data_csv) as budget_data:
    Budget_Reader = csv.reader(budget_data)
    header = next(budget_data)
    print(header) 

    # For loop to iterate over Budget data to, 
    # calculate Total Months and Total Profit.
    for row in Budget_Reader: 
        Total_Months+=1
        Total_Net_Profit = Total_Net_Profit + int(row[1])

    # Variable/List for the difference between months in profits
        Profit_Difference_List = []
        Profit_Difference = 0
        Average_Profit = 0

    # For loop to iterate through CSV and calculate the difference between profits.
    for row in Budget_Reader:
        Profit_Difference = Budget_Reader(row[1]-1)- Budget_Reader(row[1])
        Profit_Difference_list += [Profit_Difference]
    
    Sum_of_Difference = sum(Profit_Difference_List)
    Average_Profit = (Sum_of_Difference)/range(len(Profit_Difference_List)

    for row in Budget_Reader:
        if Budget_Reader(row[1]+1) > Budget_Reader(row[1]):
            Greatest_Increase = Budget_Reader(row[1]+1)
        elif Budget_Reader(row[1]+1) < Budget_Reader(row[1]):
            Greatest_Decrease = Budget_Reader(row[1]+1])

# Printing Financial Analysis Table
print("Financical Analysis")
print("-----------------")
print("Total Months: " + str(Total_Months))
print("Total: " + str(Total_Net_Profit))
print("Average Profit Gain/Loss $" + str(Average_Profit))
print("Greatest % Increase: "  + str(Greatest_Increase))
print("Greatest % Decrease: " + str(Greatest_Decrease))