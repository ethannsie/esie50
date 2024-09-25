'''Ethan Sie, Marco Quintero, Ankita Saha, Colyi Chen
  Trojan Horses
  SoftDev
  running basic flask scripts and noting differences/comments
  2024-9-23
  time spent: 0.1 hours
  '''

from flask import Flask
app = Flask(__name__)          # Creates an instance of a class

@app.route("/")                # Maps the url to "/"
def hello_world():
    print(__name__)            # Prints the current page to the terminal; Our prediction was correct
    return "No hablo queso!"   # Prints "No hablo queso!" to the server; Prediction was correct

app.run()                     # Runs the app object; Correct prediction
                
