# pylint: disable-all
from flask import Flask

app = Flask(__name__)

@app.route("/report")
def index():
    pass

@app.route("/command")
def command():
    pass
