from flask import Flask

import os

app = Flask(__name__)
@app.route("/")
def lw():
    return "<body bgcolor='aqua'><h1>I am Umang with complete pipeline...</h1></body>"

app.run(host='0.0.0.0' , port=8080)
