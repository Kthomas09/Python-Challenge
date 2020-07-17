#PyBank Python Script

#Importing CSV and OS
import os
import csv


#Budget Data Pathway
budget_data_csv =  os.path.join("PyBank/Resources/budget_data.csv")

#Variables for Total Months and Total Net Profit
total_months = 0
total_profits = 0
average_profit = 0
Greatest_Increase = 0
Greatest_Decrease = 0

#Opening 
with open(budget_data_csv) as budget_data:
    Budget_Reader = csv.reader(budget_data)
    header = next(budget_data)
        
    # For loop to iterate over Budget data to calculate Total Months and Total Profit.
    for row in Budget_Reader: 
        total_months+=1
        total_profits = total_profits + int(row[1])

    # Variable/List for the difference between months in profits
        profits = []      
        for row2 in Budget_Reader:
            profits.append(row2[1])
            break

            profit_diff = 0
            list_profit_diff =[]
# For loop to iterate through CSV and calculate the difference between profits.
            for row in range(len(profits)-1):
                profit_diff = int(profits[row+1]) - int(profits[row])
                list_profit_diff.append(profit_diff)
                break
            sum_of_profit = sum(list_profit_diff)
            average_profit = sum_of_profit/len(profits)


    # # for row in profit
    # if Budget_Reader(row[1]+1) > Budget_Reader(row[1])
    #     Greatest_Increase = (f"{Budget_Reader(row[1]+1)},{Budget_Reader(row[0]+1)}")
    # elif Budget_Reader(row[1]+1) < Budget_Reader(row[1]):
    #     Greatest_Decrease = Budget_Reader(row[1]+1])

budget_data.close()

# # Printing Financial Analysis Table
print("Financical Analysis")
print("-----------------")
print(f"Total Months: {total_months}")
print("Total: $" + str(total_profits)
print("Average Profit Gain/Loss $" + str(average_profit))
# # # print("Greatest % Increase: "  + str(Greatest_Increase))
# # # print("Greatest % Decrease: " + str(Greatest_Decrease))