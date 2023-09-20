# Create a Python script that analyzes the PyBank records to calculate each of the following:
# -->>  The total number of months included in the dataset
# -->>  The net total amount of "Profit/Losses" over the entire period
# -->>  The average of the changes in "Profit/Losses" over the entire period
# -->>  The greatest increase in profits (date and amount) over the entire period
# -->>  The greatest decrease in losses (date and amount) over the entire period
# -->>  Print the analysis to the terminal and export a text file with the results


# Import dependencies
#import os
import csv
from pathlib import Path

csv_path = Path("Resources/budget_data.csv")

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # all_lists = [row for row in csvreader]
    for row in csvreader:
        print(row[1], row[0])
    # print(all_lists)

# # Bank's 'list' variables
# number_of_months = []
# profit_loss_changes = []

# net_profit_loss = 0
# previous_month_profit_loss = 0
# current_month_profit_loss = 0
# profit_loss_change = 0
# months_counter = 0

#output file --> ../analysis/analysis_data.txt
analysis_file = Path("analysis/budget_analysis_data.txt")
with open(analysis_file, "w") as outfile:

    outfile.write("Financial Analysis\n")