# Import dependencies
import os
import csv

# Assign file location with the pathlib library
election_data_csv = os.path.join("Resources", "election_data.csv")

# Declare Variables 
total_votes = 0 
stockham_votes = 0
degette_votes = 0
doane_votes = 0

# Open csv in default read mode with context manager
with open(election_data_csv,newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Ballot ID's and store in variable  called total_votes
        total_votes +=1

        # We have three candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Charles Casper Stockham": 
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes +=1

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [stockham_votes, degette_votes, doane_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
stockham_percent = (stockham_votes/total_votes) *100
degette_percent = (degette_votes/total_votes) * 100
doane_percent = (doane_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Correy: {degette_percent:.3f}% ({degette_votes})")
print(f"O'Tooley: {doane_percent:.3f}% ({doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files
# Assign output file location
output_file = os.path.join("Analysis", "Election_Results_Summary.txt")

with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {stockham_percent:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Correy: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
