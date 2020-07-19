import os
import csv


# Set Path For File
budgetPath = os.path.join("PyBank/Resources/budget_data.csv")
analysisOutput = os.path.join("PyBank/Analysis/Analysis.text")

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
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    budgetReader = csv.reader(csvfile, delimiter=",")
    # Read The Header Row First (Skip This Step If There Is No Header)
    budgetHeader = next(budgetReader)
    row = next(budgetReader)
    # Calculate Total Number Of Months, Net Amount Of “Profit/Losses” & Set Variables For Rows
    previous = int(row[1])
    totMonths += 1
    totProfit += int(row[1])
    increase = int(row[1])
    increaseMonth = row[0]
    # Read Each Row Of Data After The Header
    for row in budgetReader:
        # Calculate Total Number Of Months Included In Dataset
        totMonths += 1
        # Calculate Net Amount Of “Profit/Losses” Over The Entire Period
        totProfit += int(row[1])
        # Calculate Change From Current Month To Previous Month
        profitChange = int(row[1]) - previous
        profitDifference.append(profitChange)
        previous = int(row[1])
        monthsList.append(row[0])
        # Calculate The Greatest Increase
        if int(row[1]) > increase:
            increase = int(row[1])
            increaseMonth = row[0]
        # Calculate The Greatest Decrease
        if int(row[1]) < decrease:
            decrease = int(row[1])
            decreaseMonth = row[0]
    # Calculate The Average & The Date
    averageChange = sum(profitDifference)/ len(profitDifference)
    highest = max(profitDifference)
    lowest = min(profitDifference)
# Print Analysis
    # print("Financial Analysis")
    # print(totProfit)
    # print(averageChange)
    # print(increaseMonth, highest)
    # print(decreaseMonth, decrease)


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

    

