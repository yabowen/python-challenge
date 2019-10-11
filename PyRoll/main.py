import os
import csv
file_load = os.path.join("..","PyRoll","election_data.csv")
file_output = os.path.join("..","PyRoll","election_results.txt")

total = 0
candidates = []
votes = {}
winner = ""
winner_vote = 0

with open(file_load, newline='') as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    #header = next(csvfile)
    
    for row in data:
        total += 1
        candidate = row["Candidate"]
        if candidate not in candidates:
            candidates = candidates + [candidate]
            votes[candidate] = 0
        votes[candidate] = votes[candidate] + 1

with open(file_output, 'w') as txt_file:
    output = (
              "\nElection Results\n"
              "-----------------------------------\n"
              f"Total Votes: {total}\n"
              "-----------------------------------\n")
              print(output)
              txt_file.write(output)
              
              for candidate in votes:
                  vote = votes.get(candidate)
                  votepct = float(vote)/float(total)*100
                  voter_detail = f"{candidate}: {votepct:.3f}% ({vote})\n"
                      
                      print(voter_detail)
                      txt_file.write(voter_detail)
                      
                      if vote > winner_vote:
                          winner_vote = vote
                              winner = candidate

winner_summary = ("-----------------------------------\n"
                  f"Winner: {winner}\n"
                  "-----------------------------------\n")
print(winner_summary)
txt_file.write(winner_summary)

