  # Tanzeem Hasan, Ethan Sie
  # To_Be_Decided
  # SoftDev
  # K23: A RESTful Journey Skyward
  # 2024-11-21
  # time spent: 20 mins

import urllib.request, json
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    data = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?date=2018-11-09&api_key=d6hAGcxE6hBZbreEovx6gS1P019bGHE43H5AfDBy")
    # print(data.info)
    w = json.loads(data.read())
    # print("check")
    return render_template('main.html', exp = w['explanation'], source=w['url'])


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
