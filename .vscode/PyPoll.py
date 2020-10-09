# add our dependencies
import csv
import os
# assign a variable to load a file
file_to_load = os.path.join("Resources","election_results.csv")
# assign a variable to save a file
file_to_save = os.path.join("analysis","election_analysis.txt")
# Open the results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read Print the header row
    headers = next(file_reader)
    print(headers)
    # 1. The total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the election based on popular vote.
