import csv
import os

#ask about this filepath
csvpath = os.path.join("election_data.csv")

voter_ids = []
counties = []
candidates = []

#opens the csv file election_data.csv
with open(csvpath, newline='', encoding='utf8') as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
    csv_header = next(csvreader)

    #populates the lists
    for row in csvreader:
        voter_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

    #converts the candidates list into a dictionary for keys
candidates_dict = list(dict.fromkeys(candidates))

#Find the number of votes each candidate had
total_votes = len(voter_ids)
Khan_num = candidates.count("Khan")
Correy_num = candidates.count("Correy")
Li_num = candidates.count("Li")
OTooley_num = candidates.count("O'Tooley")

#Convert the number of votes to percentages
Khan_perc = Khan_num / total_votes
Correy_perc = Correy_num / total_votes
Li_perc = Li_num / total_votes
OTooley_perc = OTooley_num / total_votes

#Dictionary for candidate vote numbers
candidates_dict = {'Khan': Khan_num, 'Correy': Correy_num, 'Li': Li_num, 'OTooley': OTooley_num}


#Prints the stats in Python
print(f"""
----------------
Election Results
----------------

Total Votes: {total_votes}

----------------

Khan: {round((Khan_perc * 100), 3)}% ({Khan_num})
Correy: {round((Correy_perc * 100), 3)}% ({Correy_num})
Li: {round((Li_perc * 100), 3)}% ({Li_num})
O'Tooley: {round((OTooley_perc * 100), 3)}% ({OTooley_num})

----------------
Winner: {max(candidates_dict, key=candidates_dict.get)}
""")


#Writes the stats to a text file
output_file = os.path.join("PyPoll_output.txt")
output = open(output_file, "w")
output.write(f"""
----------------
Election Results
----------------

Total Votes: {total_votes}

----------------

Khan: {round((Khan_perc * 100), 3)}% ({Khan_num})
Correy: {round((Correy_perc * 100), 3)}% ({Correy_num})
Li: {round((Li_perc * 100), 3)}% ({Li_num})
O'Tooley: {round((OTooley_perc * 100), 3)}% ({OTooley_num})

----------------
Winner: {max(candidates_dict, key=candidates_dict.get)}
""")
