import csv

dictionary = {}

with open("city-of-seattle-2012-expenditures-dollars.csv") as file:
    reader = csv.reader(file,delimiter=",")
    for line in reader:
        #if executes only if the department is not already in dictionary
        if(dictionary.get(line[0]) == None):
            n = line[0]
            j = .00
            #adds only values that are digits and not strings
            for vals in line[1:]:
                if vals.isdigit():
                    j = j + float(vals)
            dictionary[n] = j
        else:
            n = line[0]
            j = 0
            # adds only values that are digits and not strings
            for vals in line[1:]:
                if vals.isdigit():
                    j = j + float(vals)
            dictionary[n] = j + dictionary[n]

for lines in dictionary:
    if lines != "Department" and lines != "":
        moneyFormat = f"${dictionary[lines]:,.2f}"
        print(lines + " Department Total Money Spent: " + str(moneyFormat))







