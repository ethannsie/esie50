"""
Ethan Sie
Dancing Elmo
SoftDev
06_py-csv
2024-09-19
time spent: .8

Disco:
    Get the data from a csv file with:
   
    with open(file, newline='') as csvfile:
        csvFile = csv.reader(csvfile, delimiter='\n')

QCC:
    Would there be a way to directly weight the chances of
    getting certain values in a dictionary?

How This Script Works:
    The csv file is read. To convert the data to a dictionary,
    each line of the data is searched for a comma followed by
    a numeric value. The index of the comma is taken and the
    part of the string before the index is taken as a dict key
    while the remainder is taken as the dict value and cast
    into a float. To randomize a job, a random float is
    generated and stored in a variable. As the dict is traversed,
    subtracting the percentage value from the variable until it
    is less than or equal to 0. The key that causes this is the
    returned job.
"""

import csv
import random

def fileParser(file): #reads csv
    with open(file, newline='') as csvfile:
        csvFile = csv.reader(csvfile, delimiter='\n')
        data = []
        for line in csvFile:
            data.append(line)
    return data

def splitHeaders(dataSet): #converts data to dictionary
    dictValues = {}
    for data in dataSet:
        for string in data:
            for count, letter in enumerate(string[:len(string)-1]):
                if letter == ',' and string[count+1].isnumeric():
                    dictValues[string[:count]] = float(string[count+1:])
    return dictValues

def randomizeJob(dict): #randomizes job, weighted
    randVal = random.uniform(0,99.8)
    for data in dict:
        randVal -= dict[data]
        if(randVal <= 0):
            return data


jobData = fileParser('occupations.csv')
headers = jobData[0][0].split(',')
##print(headers)

numJobData = jobData[1:]
dictValues = splitHeaders(numJobData)
#print(dictValues)

randJob = randomizeJob(dictValues)
print("Job Class: " + randJob)