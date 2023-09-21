# Import dependencies
# import os, Path from pathlib, collections, and Counter from collections
# In Python, a Counter object is a part of the collections module, 
# and it's essentially a specialized dictionary used for counting the frequency of elements in a collection, 
# typically in an iterable like a list, tuple, or string. Counter is a handy tool when you want to quickly analyze the distribution of items in a collection.
import csv
from pathlib import Path
import collections
from collections import Counter

# Set PyPoll's variable sets. The variable, total_voters[] is key for the correct calculation throught the code
total_voters = []
vote_count_per_candidate = []
# Set the path by grabbing the Path(put your path here)
csv_path = Path("Resources/election_data.csv")

with open(csv_path, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_voters.append(row[2])

    # SORTED list of lists
    list_of_candidates = sorted(total_voters)

    # use Counter to find commom elements and count 'em
    cleaned_candidate_list = Counter (list_of_candidates)

    # We MUST convert Counter object to list of a list
    # Remember, the output will be a SORTED three dimensional array [x][x][x]
    vote_count_per_candidate.append(cleaned_candidate_list.most_common())

    # calculate the candidate vote percentage to the third decimal place
    # percentage = (votes per candidate x 100) / number of votes
    for item in vote_count_per_candidate:
       
        first_place_percentage = format((item[0][1])*100/(sum(cleaned_candidate_list.values())),'.3f')
        second_place_percentage = format((item[1][1])*100/(sum(cleaned_candidate_list.values())),'.3f')
        third_place_percentage = format((item[2][1])*100/(sum(cleaned_candidate_list.values())),'.3f')

#count number of total votes and assign it to variable, total_voter_count 
total_voter_count = len(total_voters)

# -->>  Print analysis to standard out
print("\n")
print("Election Results")
print("-------------------------------")
print(f"Total Votes:  {total_voter_count}")
print("-------------------------------")
print(f"{vote_count_per_candidate[0][0][0]}: {first_place_percentage}% ({vote_count_per_candidate[0][0][1]})\n")
print(f"{vote_count_per_candidate[0][1][0]}: {second_place_percentage}% ({vote_count_per_candidate[0][1][1]})\n")
print(f"{vote_count_per_candidate[0][2][0]}: {third_place_percentage}% ({vote_count_per_candidate[0][2][1]})\n")
print("-------------------------------")
print(f"Winner:  {vote_count_per_candidate[0][0][0]}")
print("-------------------------------")

#output_file --> ../analysis/poll_analysis_data.txt
analysis_file = Path("analysis/poll_analysis_data.txt")

with open(analysis_file, "w") as output_file:

    output_file.write("Election Results\n")
    output_file.write("-------------------------------\n")
    output_file.write(f"Total Votes:  {total_voter_count}\n")
    output_file.write("-------------------------------\n")
    output_file.write(f"{vote_count_per_candidate[0][0][0]}: {first_place_percentage}% ({vote_count_per_candidate[0][0][1]})\n")
    output_file.write(f"{vote_count_per_candidate[0][1][0]}: {second_place_percentage}% ({vote_count_per_candidate[0][1][1]})\n")
    output_file.write(f"{vote_count_per_candidate[0][2][0]}: {third_place_percentage}% ({vote_count_per_candidate[0][2][1]})\n")
    output_file.write("-------------------------------\n")
    output_file.write(f"Winner:  {vote_count_per_candidate[0][0][0]}\n")
    output_file.write("-------------------------------\n")  