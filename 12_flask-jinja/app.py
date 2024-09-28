"""
Ethan Sie
Elmos_Cheez-its
SoftDev
K12 - flask jinja
2024-09-26
time spent: 0.6
"""

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
Prediction: If we remove render_template, then test_tmplt() won't be able to use the render_template package, and there  would be no output on the "/my_foist_template" page.
Results: The "my_foist_template" page encounted the following error message: "NameError: name 'render_template' is not defined."
Q1:
Prediction: Yes, we can all predict the url: "127.0.0.1:5000/my_foist_template"
Results: We were correct.
Q2:
Predictions: Argument 1: The model template html displayed on the server; Argument 2: The title/name displayed of the server; Argument 3: Takes in data to be applied
Results: Argument 1: We were correct; Argument 2: It was displayed on the tab; Argument 3: We were correct
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
"""
Observations:
1. render_template is used for templating HTML files and making it easy to only change a small part of it while keeping other elements the same
2. Jinja is used to allow variables and add functionality such as loops to HTML documents
3. Variable order (besides the first one that declares the HTML template) does not matter (runs the same with the variables after the first argument mixed)
4. Variables in the HTML template are surrounded by {{}} as an indicator
5. Loops in the HTML template need to be closed (Kind of like HTML format)
6. You can use HTML elements in Jinja loops
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
QCC:
1. Are there any limitations in the types of variables that can be passed through render_template? 
2. How does flask recognize when it is Jinja and not just plaintext? (Ex. When user wants to print {{}} and not use Jinja)
3. How does it combine loop elements with HTML elements (template file loops and repeatedly prints a break after each argument)
4. Does render_template return the HTML elements as a string or the HTML file itself?
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', collection=coll, foo = "fooooo")


if __name__ == "__main__":
    app.debug = True
    app.run()

