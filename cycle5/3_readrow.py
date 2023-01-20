import csv
f = open("sample0.csv","r")
list =[]

fcsv =csv.reader(f) #creates a list with items as list of each rows

for row in fcsv:
	print(row)

print(list)	

