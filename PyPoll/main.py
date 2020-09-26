# Import dependencies for file i/o and csv files
import os
import csv

# Assumption: Voter ID read in from CSV file is unique
# That is each line represents one unique vote
# Would not be very useful data if Voter ID was not unique
# In real world scenarios would check this and clean data first

# Set up dictionary for candidate names and their votes
# Candidate name is key for dictionary
# Assumes that candidate names are unique in CSV file
# Voting would not work properly otherwise
candidate_votes = {}

# Initialise total vote count to 0
total_votes = 0

# Create path to CSV input file
csvpath = os.path.join("Resources", "election_data.csv")

# Read CSV file in using with open
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first of Voter ID, County and Candidate
    csv_header = next(csvreader)

    # Read each row of election data after the header
    for row in csvreader:
        
        # Set candidate name to Candidate field i.e. row[2] from current row
        candidate_name = row[2]
        
        # Check if candidate's name is already in dictionary
        # If so increment candidate's vote count by 1
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
        # Otherwise add new candidate's name to dictionary
        # And initialise their vote count to 1
        else:
            candidate_votes[candidate_name] = 1
        
        # With each row add 1 to the number of total votes
        total_votes = total_votes + 1


# Set variable for text output file named "analysis.txt" in folder analysis
output_file = os.path.join("analysis","analysis.txt")

# Print to screen and output file
# Open the output file
# Need to append newlines to each line in file to have correctly formatted output
with open(output_file, "w") as outfile:

    # Print out headings and dashes for results
    # To screen
    print("Election Results")
    print("-------------------------")
    
    # To output file
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    
    # Print out total number of votes cast and dashes
    # To screen
    print(f"Total Votes = {total_votes}")
    print("-------------------------")

    # To output file
    outfile.write(f"Total Votes = {total_votes}\n")
    outfile.write("-------------------------\n")
    
    # max_candidate is the candidate with the most number of votes
    # Initialise to be empty string
    max_candidate = ""

    # Initialise maximum number of votes to 0
    # Ensures it is set to the first candidate upon entering loop
    max_votes = 0

    # Iterate over key and value for each candidate in dictionary
    for candidate, votes in candidate_votes.items():

        # If maximum number of votes is less than the current candidate's votes
        # Set current maximum vote getting candidate to current candidate
        # Set max_votes to current candidate's votes
        if (max_votes < votes):
                max_candidate = str(candidate)
                max_votes = votes
            
        # Format the percentage of votes as percentage with three decimal places
        # Calculated by dividing current candidate's votes by total votes
        percent_votes = "{:.3%}".format(votes/total_votes)
    
        # Print out candidate, percentage of votes obtained and raw number of votes
        # To screen
        print(f"{candidate}: {percent_votes} ({votes})")
    
        # To output file
        outfile.write(f"{candidate}: {percent_votes} ({votes})\n")
    
    
    # Print out separation line
    # To screen
    print("-------------------------")
    
    # To output file
    outfile.write("-------------------------\n")
    

    # Print out name of winning candidate stored in max_candidate
    # To screen
    print(f"Winner: {max_candidate}")

    # To output file
    outfile.write(f"Winner: {max_candidate}\n")

    # Print out separation line
    # To screen
    print("-------------------------")
    
    # To output file
    outfile.write("-------------------------\n")
    
    
