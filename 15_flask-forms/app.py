"""
Finding Elmo: Ethan Sie, Aidan Wong, Qianjun Zhou
SoftDev
K15 - Flask Inputs With Different Requests
2024-10-08
time spent: 0.8
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template('login.html')

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    name = request.form.get('name') if request.method == 'POST' else request.args.get('name')
    return render_template('response.html', name=name)

if __name__ == "__main__":
    app.debug = True
    app.run()
