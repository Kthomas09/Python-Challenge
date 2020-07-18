#PyBank Python Script

#Importing CSV and OS
import os
import csv


#Budget Data Pathway
budget_data_csv =  os.path.join("PyBank/Resources/budget_data.csv")

#Opening 
with open(budget_data_csv) as budget_data:
    budget_reader = csv.reader(budget_data)
    header = next(budget_data)
    
    # empty lists to be populated by for loops for easier calcuation
    months = []
    profits =[]
    profitdiff = []
    greatestincrease = ["",0]
    greatestdecrease = ["". 99999999]

    # Global Variables
    total_profit = 0
    difference = 0
   

    # for loop to populate the empty lists above + total profit
    for row in budget_reader:
        months.append(row[0])
        profits.append(row[1])
        total_profit = total_profit + int(row[1])
        

    # for loop to calculate the difference of profit change
    for row in range(len(profits)-1):
        difference = int(profits[row+1]) - int(profits[row])
        profitdiff.append(difference)
    # calculations for average net profit
    sumofprofit = sum(profitdiff)
    averageprofit = sumofprofit/len(profitdiff)
    formattedaverage = "{:.2f}".format(averageprofit)

    
            





    # print(months)
    # print(profits)
    # print(total_profit)
    # print(profitdiff)
    print(formattedaverage)

