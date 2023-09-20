# Create a Python script that analyzes the votes and calculates each of the following:
# -->>  The total number of votes cast
# -->>  A complete list of candidates who received votes
# -->>  The percentage of votes each candidate won
# -->>  The total number of votes each candidate won
# -->>  The winner of the election based on popular vote

# Import dependencies
#import os
import csv
from pathlib import Path

csv_path = Path("Resources/election_data.csv")

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # all_lists = [row for row in csvreader]
    for row in csvreader:
        print(row[2], row[1], row[0])
    # print(all_lists)


    # -----

#output file --> ../analysis/poll_analysis_data.txt
analysis_file = Path("analysis/poll_analysis_data.txt")

with open(analysis_file, "w") as outfile:

    outfile.write("Election Results\n")