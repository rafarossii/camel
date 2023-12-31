from flask import Flask
import subprocess
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'ola'

@app.route('/camel/<email>')
def camel(email):
    arquivo = random.choice(['camel.py', 'camel2.py', 'camel3.py'])
    result = subprocess.run(["python", arquivo, email], capture_output=True, text=True)
    return result.stdout
