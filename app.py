from flask import Flask
from flask import render_template
import logging
import os

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def hello_world():
    print('hello')
    logging.debug('hello')
    logging.debug('I am really really loving this!')
    logging.debug('And yet another item!')
    return render_template("index.html")

@app.route('/test')
def my_world():
    logging.debug(os.environ.get('MYVAR'))
    logging.debug('My world test!')
    logging.error('Another logging entry!')
    return 'My World!  Super simple error log'
