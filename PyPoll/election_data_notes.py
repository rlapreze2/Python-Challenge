#  import csv module
import csv

# set path for file
election_file_path = "PyPoll/Resources/election_data.csv"

# set variables
total_votes = 0
candidates = []
header = []
candidates_votes = {} # key is candidate name, value is vote count
votes = 0
max_votes = 0
percentage = 0
candidates_percentage = {}
winner = str()

# open csv file and read it 
with open(election_file_path, 'r') as election_file:
    
    # store contents of the csv file into csv_file
    csv_file = csv.reader(election_file)

    # skips the header row, stores column headers in header
    header = next(csv_file)

    # read a row in the file, loop through each row
    for row in csv_file:
        
        # add to total votes
        # counts the number of rows to sum up total votes
        total_votes += 1

        # "Ballot ID,County,Candidate"
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        
        # check to see if the candidate exists
        if candidate not in candidates:
            # add to list if they haven't been added to the list
            candidates.append(candidate)

        # check to see if the candidate exists in the dictionary (same as comic book)
        if candidate not in candidates_votes:
            candidates_votes[candidate] = 1
        else:
            # sum up votes for each candidate
            candidates_votes[candidate] += 1

# test print total_votes to terminal
print(total_votes)

# test print candidate names to terminal
print(candidates)

# test print dict of candidate name and votes
print(candidates_votes)

# search for candidate name in the candidate_votes dict (to calc % of votes and winner)
for candidate in candidates_votes.keys():

    # store vote count for each candidate as int
    votes = candidates_votes[candidate]
    # print(votes) #prints the votes count as int

    # calc % of votes
    percentage = (votes / total_votes) * 100

    # store percentage in a new dict, key is candidate name and value is percentage
    candidates_percentage[candidate] = percentage
 
    # test print candidate percentage of votes to terminal
    print(candidates_percentage)

    # calc winner based on popular vote
    if votes > max_votes:
        max_votes = votes
        winner = candidate
    
    # test print winner to terminal
    print(winner)

# candidates_votes = {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}
# candidates_percentages = {'Charles Casper Stockham': 23.049, 'Diana DeGette': 73.812, 'Raymon Anthony Doane': 3.139}

out_file_path = "PyPoll/Analysis/election_data_analysis.txt"

with open(out_file_path, 'w') as analysis:
    # write header and total votes
    analysis.write('Election Results\n')
    analysis.write('-----------------------------------\n')
    analysis.write(f'Total Votes: {total_votes}\n')
    analysis.write('-----------------------------------\n')
    
    # write each candidate's result
    for candidate in candidates_votes:
        votes = candidates_votes[candidate]
        percentage = candidates_percentage[candidate]
        analysis.write(f'{candidate}: {percentage:.3f}% ({votes})\n')

    # write the winner
    analysis.write('-----------------------------------\n')
    analysis.write(f'Winner: {winner}\n')
    analysis.write('-----------------------------------\n')