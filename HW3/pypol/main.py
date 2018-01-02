import os
import csv

csvpath = os.path.join("pypoll", "election_data_2.csv")

candidates = []
votecount = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)


    for row in csvreader:
        candidates.append(row[2])


totalvotes = len(candidates)


candidatelist = list(set(candidates))

votecount1 = 0

for x in range(0,len(candidates)):
	if (candidates[x] == candidatelist[1]):
		votecount1 = votecount1 + 1
	else:
		votecount1 = votecount1
	
#from pprint import pprint	
from collections import Counter


print("Election Results")
print("--------------------------")
print("Total Votes: " +str(totalvotes))
print("--------------------------")


totals = Counter(candidates)
totals.keys()

for key, value in totals.items():
	print(str(key) + " :     %" + str(round(100*int(value)/totalvotes,2)) + "     (" + str(value) + ")")

from statistics import mode

print("--------------------------")
print("Winner: " + mode(candidates))
print("--------------------------")
