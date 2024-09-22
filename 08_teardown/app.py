'''
Ethan Sie
Dancing Elmo
SoftDev
08_teardown
2024-09-20
time spent: .5
'''

'''
DISCO:
<note any discoveries you made here... no matter how small!>
1. We discovered that whenever the linked server is accesssed/refreshed, "__main__
127.0.0.1 - - [21/Sep/2024 14:39:47] "GET / HTTP/1.1" 200 -" will get printed to the terminal.
2. We cannot run inspect on the webpage in the browser.

QCC:
0. We have seen similar syntax in C#/Java in creating instances of classes.
1. One point of reference of the '/', is that it represents the root directory. It also acts as a separator in a url. This resembles the home page, index.html in web development.  
2. It prints to the terminal/shell where the Flask server is running
3. It prints "_main_"
4. It appears as the first line printed on "127.0.0.1:5000." We figured this out as we observed it present when we pressed the link.
5. We have seen similar constructs of 'app.run()' as methods accessed on an object to achieve a certain action.
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?
