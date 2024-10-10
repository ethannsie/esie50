"""
Elmos_Cheez-its: Amanda Tan, Ethan Sie, Aidan Wong
SoftDev
K16 - Flask Sessions
2024-10-09
time spent: 1.0
"""

from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

sessions = {}

users = {
    'Aidan': 'bill',
    'Amanda': 'law',
    'Ethan': 'order'
}

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        print(name)
        print(password)

        if name in users and users[name] == password:
            session_id = os.urandom(16)
            sessions[session_id] = {'username': name}
            session['session_id'] = session_id
            return redirect('/home')

        return redirect('/') # Used to remove the confirm form resubmission pop up when page is refreshed after entering incorrect data
    if 'session_id' in session:
        return redirect('/home')
    return render_template('login.html')


@app.route("/home", methods=['GET', 'POST'])
def authenticate():
    if 'session_id' in session:
        if session['session_id'] in sessions:
            returnName = sessions[session['session_id']]['username']
            return render_template('response.html', username=returnName)
    return redirect('/')

@app.route("/logout", methods=['GET', 'POST'])
def disp_logoutpage():
    if 'session_id' in session:
        returnName = sessions[session['session_id']]['username']
        session.pop('session_id')
        return render_template('logout.html', username=returnName)
    return redirect('/')



if __name__ == "__main__":
    app.debug = True
    app.run()
