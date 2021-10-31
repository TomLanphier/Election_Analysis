# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. The voter turnout for each county
# 7. The percentage of votes from each vounty out of the total count
# 8. The county with the highest turnout

# Importing dependencies
import csv
import os

# Assign variable to load results from a path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Initialize a candidate list
candidate_options = []

# Initialize a candidate vote dictionary
candidate_votes = {}

# Initialize a county list
county_list = []

# Initialize a county vote dictionary
county_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Largest county and county voter turnout tracker
largest_county = ""
largest_count = 0
largest_percentage = 0

# Open and read results file
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1

        # Set variable to the candidate's name
        candidate_name = row[2]

        # Set variable to the county's name
        county_name = row[1]

        # Determines if candidate has been added to list
        if candidate_name not in candidate_options:

            # Adds candidates name to list of candidates
            candidate_options.append(candidate_name)
            
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Determine if county has been added to list
        if county_name not in county_list:

            # Adds candidates name to list of candidates
            county_list.append(county_name)
            
            # Begin tracking that candidate's vote count
            county_votes[county_name] = 0
        
        # Add a vote to that candidate's count.
        county_votes[county_name] += 1            

# Save results to text file
with open(file_to_save, "w") as txt_file:

    # Create a header and total vote count variable
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    # Print the total votes to the terminal
    print(election_results, end="")
    
    # Save total votes to text file
    txt_file.write(election_results)

    for county_name in county_votes:
        
        # Retrieve vote count of a county
        voters = county_votes[county_name]

        # Calculate the percentage of votes
        voter_percentage = int(voters) / int(total_votes) * 100

        # Create variable of the county name, percentage of votes, and number of votes
        county_results = (f"{county_name}: {voter_percentage:.1f}% ({voters:,})\n")

        # Print each county, their vote count, and percentage to the terminal
        print(county_results)

        #  Save the county results to our text file
        txt_file.write(county_results)

        # Check if this candidate has the most votes
        if (voters > largest_count) and (voter_percentage > largest_percentage):
            # Set candidate's values to winning variables
            largest_county = county_name
            largest_count = voters
            largest_percentage = voter_percentage

    # Print the largest county's name, votes, and percentage
    largest_county_summary = (
        f"-------------------------\n"
        f"County with Highest Voter Turnout: {largest_county}\n"
        f"-------------------------\n")
    
    # Print the largest county's name, votes, and percentage to the terminal
    print(largest_county_summary)

    # Save the largest county's name, votes, and percentage to text file
    txt_file.write(largest_county_summary)


    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        
        # Calculate the percentage of votes
        vote_percentage = int(votes) / int(total_votes) * 100
        
        # Create variable of the candidate name, percentage of votes, and number of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their vote count, and percentage to the terminal
        print(candidate_results)

        #  Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Check if this candidate has the most votes
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # Set candidate's values to winning variables
            winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percentage

    # Print the winning candidate's name, votes, and percentage
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    # Print the winning candidate's name, votes, and percentage to the terminal
    print(winning_candidate_summary)

    # Save the winning candidate's name, votes, and percentage to text file
    txt_file.write(winning_candidate_summary)

