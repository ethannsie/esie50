"""
Ethan Sie
Elmos_Cheez-its
SoftDev
K11 - Static Flask Pages
2024-09-25
time spent: 0.5
"""

# DEMO
# basics of /static folder
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return f"""
    <head>
        <title>Root</title>
    </head>
    No hablo queso! 
    <br>
    <a href="static/foo.html"> Go to foo </a>
    <br>
    <a href="static/fixie.html"> Go to fixie </a>
    """

# Prints a random number between 0 and 1 when foo.html is requested; Overwrites the HTML on the page that says "Is this plaintext, though?"
# Name of the module is __main__
'''
@app.route("/static/foo.html")
def h():
    print("the __name__ of this module is... ")
    print(__name__)
    return str(random.random())
'''

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

