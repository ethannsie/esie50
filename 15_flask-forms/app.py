"""
Elmos_Cheez-its: Amanda Tan, Ethan Sie, Aidan Wong
SoftDev
K14 - User Input with Flask
2024-10-07
time spent: 0.7
"""

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import testmod0

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will not.

TASK:
 Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST']) # Flask defaults to GET (shown in flask terminal on page load); POST likely used to submit things back to the server (as GET is used to retrieve things from the server) -> Can be used to give data from a form to the server to use in a HTML document
def disp_loginpage():
#     print("\n\n\n")
#     print("***DIAG: this Flask obj ***")
#     print(app) # Prints <Flask 'app'>
#     print("***DIAG: request obj ***")
#     print(request) # Prints <Request 'http://127.0.0.1:5000/' [GET]> 127.0.0.1 - - [07/Oct/2024 21:04:20] "GET / HTTP/1.1" 200 -
#     print("***DIAG: request.args ***")
#     print(request.args) # Prints ImmutableMultiDict([]) => Datatype of previous print(request), dosen't have anything inside because no args
#     print("***DIAG: request.args['username']  ***")
#     print(request.args['username']) # Leads to a BadRequestKeyError likely due to the lack of a username query paramater in the URL => Confirmed, When placing ?username=J into the URL, Code functions as normal and terminal prints J (the username)
#     print("***DIAG: request.headers ***")
#     print(request.headers) # Prints information about the browser, host, connection type, system and some more cryptic things
    return render_template( 'login.html' )

# When visitng this page through the URL (host/auth), it returns errors when requesting the username, as it is not given (similar to the index)
@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) # Same <Flask 'app'>
    print("***DIAG: request obj ***")
    print(request) # Returns the URL with the same GET request
    print("***DIAG: request.args ***")
    print(request.args) # Returns the ImmutableMultiDict with the username and username value sin one list, and the input submit type of the HTML and its corresponding name
    print("***DIAG: request.args['username']  ***")
    print(request.args['username']) # Shows the username
    print("***DIAG: request.headers ***")
    print(request.headers) # Shows the same information as before
    print(request.form)
    # When this functiaonlity is added, it makes the auth page more personalized for users, but also increases the vulnerabilities as nothing sanitizes the username input
    username = request.args.get('username') # Considers the empty box an empty string? => Works Regardless of what is submitted
    return f"Waaaa hooo HAAAH {username}"  #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
