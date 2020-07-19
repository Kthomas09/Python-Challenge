# PyBank Script
# Objective: 1) Calculate Total Months
#            2) Total Profit
#            3) Average change in profit. (subtract change, create list, add list, divide by length)   
#            4) Maximum increase in profit change (Print Mon. and Date)
#            5) Maximum decrease in profit change (Print Mon. and Date)

# Import modules
import os
import csv


# Set input and output pathways
budgetPath = os.path.join("PyBank/Resources/budget_data.csv")
analysisOutput = os.path.join("PyBank/Analysis/Financial Analysis.text")

# Variables
totMonths = 0
totProfit = 0
profitDifference= []
monthsList = []
increase = 0
increaseMonth = 0
decrease = 0
decreaseMonth = 0

# Open & Read CSV File
with open(budgetPath, newline="") as csvfile:
    # Variable reads CSV File and specifies delimiter
    budgetReader = csv.reader(csvfile, delimiter=",")
    # Variable to Skip Header
    budgetHeader = next(budgetReader)
    # Variable to skip row. This is used in the Average Calculation.
    row = next(budgetReader)
    # variables for total Months, total Profit, and  specify locations in DataSet
    previous = int(row[1])
    totMonths += 1
    totProfit += int(row[1])
    increase = int(row[1])
    increaseMonth = row[0]
    # Read each row of usuable data
    for row in budgetReader:
        # Calculate Total Number Of Months
        totMonths += 1
        # Calculate Net “Profit/Losses” over data period
        totProfit += int(row[1])
        # Calculate the difference of current month to previous month and create the profitDifference and monthList
        profitChange = int(row[1]) - previous
        profitDifference.append(profitChange)
        previous = int(row[1])
        monthsList.append(row[0])
        # Calculate The Maximum Increase
        if int(row[1]) > increase:
            increase = int(row[1])
            increaseMonth = row[0]
        # Calculate The Maximum Decrease
        if int(row[1]) < decrease:
            decrease = int(row[1])
            decreaseMonth = row[0]
    # Calculate The Average & Month/Year
    averageChange = sum(profitDifference)/ len(profitDifference)
    highest = max(profitDifference)
    lowest = min(profitDifference)

    output = (
        f"Financial Analysis\n"
        f" ----------------------\n"
        f"Total Months: {totMonths}\n"
        f"Total: ${totProfit}\n"
        f"Average Change: ${averageChange}\n"
        f"Greatest Increase in Profits:, {increaseMonth}, (${highest})\n"
        f"Greatest Decrease in Profits:, {decreaseMonth}, (${lowest})\n")

with open(analysisOutput, "w",) as txt_file:
    txt_file.write(output)

    

