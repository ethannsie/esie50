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

