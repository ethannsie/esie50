"""
Ethan Sie
Dancing Elmo
SoftDev
06_py-csv
2024-09-19
time spent:
"""

import csv

def fileParser(file):
    with open(file, newline='') as csvfile:
        csvFile = csv.reader(csvfile, delimiter='\n')
        data = []
        for line in csvFile:
            data.append(line)
    return data

def splitHeaders(dataSet):
    dictValues = {}
    for data in dataSet:
        for string in data:
            for count, letter in enumerate(string[:len(string)-1]):
                if letter == ',' and string[count+1].isnumeric():
                    dictValues[string[:count]] = float(string[count+1:])
    return dictValues


jobData = fileParser('occupations.csv')
headers = jobData[0][0].split(',')
##print(headers)
numJobData = jobData[1:]
dictValues = splitHeaders(numJobData)
print(splitHeaders(numJobData))


