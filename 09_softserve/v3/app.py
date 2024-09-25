# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...") #Verified in last version; will print in the terminal
    print(__name__)                   #This goes to terminal!
   # print(120 + "sdfs")              # Testing that the debugger works!
    return "No hablo queso!"

app.debug = True          # We predict that this toggles app.debug on and will print a debug message to the server if there's an error within the code above
app.run()                 # We found that if there's an error within the app object, then app.debug will print a more detailed error response to the flask server 127.0.0.1:5000
