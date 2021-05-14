from flask import Flask, request
from flask import render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import logging
import os
import requests
import json

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye"),
    "gern": generate_password_hash("well"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route("/")
def hello_world():
    print('hello')
    logging.debug('hello')
    logging.debug('I am really really loving this!')
    logging.debug('And yet another item!')
    return render_template("index.html")

@app.route('/json-example', methods=['POST'])
@auth.login_required
def json_example():
    request_data = request.get_json()
    logging.debug('json-example payload')
    logging.debug(request_data)

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           I am so digging this!!!!!
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


@app.route('/test')
def my_world():
    logging.debug(os.environ.get('MYVAR'))
    logging.debug('My world test!')
    logging.error('Another logging entry!')
    return 'My World!  Super simple error log and it works great!'

@app.route('/api_test/<value>')
def my_api_test(value):
    logging.debug('Starting my_api_test')
    logging.debug(f"The value is:{value}")
    logging.debug(f"I am digging this!!!")
    value = int(value)
    my_dict = {"parameter": "temp", "value": value}
    json_result = json.dumps(my_dict)
    
    return json_result

@app.route('/json_test/<id>')
@auth.login_required
def my_new_world(id):
    id = int(id)
    my_dict = {"alpha": id, "beta": "goodbye",}
    return json.dumps(my_dict)

if __name__ == "__main__":
    app.run()
