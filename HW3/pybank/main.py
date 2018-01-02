import os
import csv

number_of_files = input("How many input files?")

for y in range(1,int(number_of_files)+1):

	csvpath = os.path.join("pybank", "budget_data_" + str(y) + ".csv")


	months = []
	revenue = []
	revenuechange = []



	# Open the CSV
	with open(csvpath, newline="") as csvfile:
	    csvreader = csv.reader(csvfile, delimiter=",")

	    for row in csvreader:
	        months.append(row[0])
	        revenue.append(row[1])



	totalrevenue = 0
	for x in range(1,len(months)):
		totalrevenue = totalrevenue + int(revenue[x])




	#print(revenue)
	#print(revenue[1])

	for x in range(2,len(months)):
		revenuechange.append(int(revenue[x])-int(revenue[x-1]))

	average_revenue_change = sum(revenuechange)/len(revenuechange)
	max_revenue_increase = max(revenuechange)
	max_revenue_decrease = min(revenuechange)

	#print(revenuechange)

	print("Financial Analysis")
	print("------------------------------------")
	print("Total Months: " + str(len(months)))
	print("Total Revenue: $" + str((totalrevenue)))
	print("Average Revenue change: $" +str(average_revenue_change))
	print("Greatest Increase in Revenue: $" +str(max_revenue_increase))
	print("Greatest Decrease in Revenue: $" +str(max_revenue_decrease))