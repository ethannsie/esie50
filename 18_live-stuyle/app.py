"""
Elmos_Cheez-its: Amanda Tan, Ethan Sie, Aidan Wong
SoftDev
K18 - CSS Styling with Flask
2024-10-16
time spent: 0.2
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def disp_loginpage():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
