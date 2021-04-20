from flask import Flask
from flask import render_template
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def hello_world():
    print('hello')
    logging.debug('hello')
    return render_template("index.html")
