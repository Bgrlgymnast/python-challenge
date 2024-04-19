import os
import csv

#set variables for candidate name and ballot id
total_votes = 0
candidate = ""  # candidates are the key
candidate_votes = {} # dictionary
candidate_percentage ={} # dictionary
winner_votes = 0
winner = ""


csvpath = os.path.join("python-challenge\PyPoll\Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    headers = next(csvreader) 

# Calculate vote count total
    for x in csvreader:    
       
        total_votes = total_votes + 1  
        candidate = x[2]
      
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1

        else: candidate_votes[candidate] = 1

# Calclulate vote percentage
    for candidate, vote_count in candidate_votes.items():
        candidate_percentage[candidate] = round(((vote_count/total_votes) * 100), 3)
        if vote_count > winner_votes:
            winner_votes = vote_count
       
# Identify Winner
            winner = candidate


print(f"Election Results\n")

print("----------------\n")

# #Print total votes
print(f"Total Votes: {total_votes}\n")

print("----------------\n")

for candidate, percent in candidate_percentage.items():
    print(f"{candidate}: {percent}% ({candidate_votes[candidate]})\n")

print("-----------------\n")

# #Print Winner
print(f"Winner: {winner}\n")

#Print to output file
output_file_path = os.path.join("python-challenge\PyPoll\Analysis", "Pyrolloutput.txt")

#open to file as a writeable and write the output into thefile
with open(output_file_path,"w") as output_file:
    output_file.write(f"Election Results\n")
    output_file.write("----------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("----------------\n")
    for candidate, percent in candidate_percentage.items():
        output_file.write(f"{candidate}: {percent}% ({candidate_votes[candidate]})\n")
    output_file.write("-----------------\n")
    output_file.write(f"Winner: {winner}\n")
