from flask import Flask
from flask import render_template
import logging
import os
import requests
import json

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

@app.route('/api_test/<value>')
def my_api_test(value):
    logging.debug('Starting my_api_test')
    logging.debug(f"The value is:{value}")
    my_dict = {"parameter": "temp", "value": value}
    json_result = json.dumps(my_dict)
    
    return json_result
