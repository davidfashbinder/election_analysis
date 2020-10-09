# add our dependencies
import csv
import os
# assign a variable to load a file
file_to_load = os.path.join("Resources","election_results.csv")
# assign a variable to save a file
file_to_save = os.path.join("analysis","election_analysis.txt")
# Add a total vote counter
total_votes = 0 
# Create a candidate list
candidate_options=[]
# Create a dictionary to store the votes by candidate
candidate_votes={}
#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read  the header row
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
    # 1. Total votes
        #a. Increment the total votes by 1 after the for loop
        total_votes += 1
    # 2. Total Votes by Candidate
    # Determine which candidate is on each row
        candidate_name=row[2]
    #if the candidate isn't on the list yet
        if candidate_name not in candidate_options:
            #add it to the list
            candidate_options.append(candidate_name)
            #start tracking their votes
            candidate_votes[candidate_name] = 0
        #add 1 to the candidates vote count
        candidate_votes[candidate_name] += 1
    # 3. Percentage Votes by Candidate
    # loop through the votes list
    for candidate_name in candidate_votes:
        #get the vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        #determine if votes are greater than the winning count
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    print(winning_candidate_summary)


