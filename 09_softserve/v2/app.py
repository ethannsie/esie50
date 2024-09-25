'''Ethan Sie, Marco Quintero, Ankita Saha, Colyi Chen
  Trojan Horses
  SoftDev
  running basic flask scripts and noting differences/comments
  2024-9-23
  time spent: 0.1 hours
  '''

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...") #Will print into the terminal
    print(__name__)               #This will print the current __name__ into the terminal below the previous print statement
    return "No hablo queso!"

app.run()
