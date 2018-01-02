import os
import csv

us_state_abbrev = {

    'Alabama': 'AL',

    'Alaska': 'AK',

    'Arizona': 'AZ',

    'Arkansas': 'AR',

    'California': 'CA',

    'Colorado': 'CO',

    'Connecticut': 'CT',

    'Delaware': 'DE',

    'Florida': 'FL',

    'Georgia': 'GA',

    'Hawaii': 'HI',

    'Idaho': 'ID',

    'Illinois': 'IL',

    'Indiana': 'IN',

    'Iowa': 'IA',

    'Kansas': 'KS',

    'Kentucky': 'KY',

    'Louisiana': 'LA',

    'Maine': 'ME',

    'Maryland': 'MD',

    'Massachusetts': 'MA',

    'Michigan': 'MI',

    'Minnesota': 'MN',

    'Mississippi': 'MS',

    'Missouri': 'MO',

    'Montana': 'MT',

    'Nebraska': 'NE',

    'Nevada': 'NV',

    'New Hampshire': 'NH',

    'New Jersey': 'NJ',

    'New Mexico': 'NM',

    'New York': 'NY',

    'North Carolina': 'NC',

    'North Dakota': 'ND',

    'Ohio': 'OH',

    'Oklahoma': 'OK',

    'Oregon': 'OR',

    'Pennsylvania': 'PA',

    'Rhode Island': 'RI',

    'South Carolina': 'SC',

    'South Dakota': 'SD',

    'Tennessee': 'TN',

    'Texas': 'TX',

    'Utah': 'UT',

    'Vermont': 'VT',

    'Virginia': 'VA',

    'Washington': 'WA',

    'West Virginia': 'WV',

    'Wisconsin': 'WI',

    'Wyoming': 'WY',

}


EmpID = []
Name = []
DOB = []
formattedDOB = []
SSN = []
formattedSSN = []
State = []
formattedState = []
splitname = []
lastname = []
firstname = []


y = 1

csvpath = os.path.join("pyboss", "employee_data" + str(y) + ".csv")

with open(csvpath, newline="") as csvfile:
	    csvreader = csv.reader(csvfile, delimiter=",")

	    for row in csvreader:
        	EmpID.append(row[0])
        	Name.append(row[1])
        	DOB.append(row[2])
        	SSN.append(row[3])
        	State.append(row[4])

#print(Name)
for y in range(1,len(Name)):
	splitname.append(Name[y].split())

for y in range(1,len(splitname)):
	lastname.append(splitname[y][1])

for y in range(1,len(splitname)):
	firstname.append(splitname[y][0])

for y in range(1,len(DOB)):
	formattedDOB.append(DOB[y][5:7]+"/"+DOB[y][8:10]+"/"+DOB[y][0:4])

for y in range(1,len(SSN)):
	formattedSSN.append("***-**-"+SSN[y][7:11])

for y in range(1,len(splitname)):
	formattedState.append(us_state_abbrev[State[y]])

for y in range(1,len(splitname)-1):
	print(EmpID[y] + "," + str(firstname[y]) + "," + str(lastname[y])  + "," + formattedDOB[y] + "," + formattedSSN[y] + "," + formattedState[y])
