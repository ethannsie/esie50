#Leon Huang, Evan CHan, Ethan Sie
#The Grizzly Bears
#SoftDev
#K13 - Combine
#2024-9-30
#Time Spent: TBD

from flask import Flask, render_template
import random
import csv

################################# Code from Dancing Elmos!

def fileParser(file): #reads csv
    with open(file, newline='') as csvfile:
        csvFile = csv.reader(csvfile, delimiter='\n')
        data = []
        for line in csvFile:
            data.append(line) # Puts all of the data from the csv into the list
    return data

def splitHeaders(dataSet): #converts data to dictionary
    dictValues = {}
    for data in dataSet:
        for string in data:
            for count, letter in enumerate(string[:len(string)-1]):
                if letter == ',' and string[count+1].isnumeric():
                    dictValues[string[:count]] = float(string[count+1:]) #Takes each input and enters it as a Job:Percentage dictionary
    return dictValues

def randomizeJob(dict): #randomizes job, weighted
    randVal = random.uniform(0,99.8)
    for data in dict:
        randVal -= dict[data]
        if(randVal <= 0):
            return data

###################################################

app = Flask(__name__)           #create instance of class Flask

CSV_FILE_PATH = 'data/occupations.csv'

@app.route("/")
def showHome():
    return "Welcome to the abyss"

@app.route("/wdywtbwygp")
def showT():
    jobData = fileParser(CSV_FILE_PATH) #Parses csv data
    headers = jobData[0][0].split(',') #Initial delimit
    numJobData = jobData[1:len(jobData)-1] #Cuts out the header and "Total"
    dictValues = splitHeaders(numJobData) #Converts into dictinoary
    randJob = randomizeJob(dictValues) #Finds random job
    team = ["Ethan Sie", "Evan Chan", "Leon Huang"]
    return render_template('tablified.html', teamMembers = team, foo="Grow up", teamname="The Grizzly Bears",collection = dictValues.keys())




if __name__ == "__main__":
    app.debug = True
    app.run()
