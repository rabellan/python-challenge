# Create a Python script that analyzes the PyBank records to calculate each of the following:
# -->>  The total number of months included in the dataset
# -->>  The net total amount of "Profit/Losses" over the entire period
# -->>  The average of the changes in "Profit/Losses" over the entire period
# -->>  The greatest increase in profits (date and amount) over the entire period
# -->>  The greatest decrease in losses (date and amount) over the entire period
# -->>  Print the analysis to the terminal and export a text file with the results


# Import dependencies
import csv
from pathlib import Path

csv_path = Path("Resources/budget_data.csv")

# Initialize variables
overall_profit_losses = 0
previous_month_profit_loss = 0
# Creating lists makes it easier to find Maximum and Minimum
# Calculate the number of months with an accumulator
change_in_profit_losses = []
months = []

# Read the CSV file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header!
    next(csvreader)

    for row in csvreader:
        # Extract data from the current row
        date, profit_loss = row[0], int(row[1])
        # this is the month accumulator
        months.append(date)

        # Calculate the change in profit/loss since the previous month
        if previous_month_profit_loss != 0:
            change = profit_loss - previous_month_profit_loss
            change_in_profit_losses.append(change)

        # Update the overall profit/loss
        overall_profit_losses += profit_loss

        # Store the current month's profit/loss for the next iteration
        previous_month_profit_loss = profit_loss

# Find greatest increase & decrease in profits
max_increase = max(change_in_profit_losses)
max_decrease = min(change_in_profit_losses)

# Find the months of greatest increase and decrease in profits
max_increase_month = months[change_in_profit_losses.index(max_increase)]
max_decrease_month = months[change_in_profit_losses.index(max_decrease)]

# Calculate the average change in profit/loss
avg_change = round(sum(change_in_profit_losses) / len(change_in_profit_losses), 2)

# Calculate the total number of months
total_months = len(months)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${overall_profit_losses}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

# Write the results to an output file
with open("analysis/budget_analysis.txt", "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${overall_profit_losses}\n")
    textfile.write(f"Average Change: ${avg_change}\n")
    textfile.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")
