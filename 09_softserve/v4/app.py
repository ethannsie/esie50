'''Ethan Sie, Marco Quintero, Ankita Saha, Colyi Chen
  Trojan Horses
  SoftDev
  running basic flask scripts and noting differences/comments
  2024-9-23
  time spent: 0.1 hours
  '''

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change; We found this to be true and also that the debugger will print to the terminal that the code has been changed
    app.run()
