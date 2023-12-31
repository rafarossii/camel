from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_data():
    url = "https://grandiose-polydactyl-emperor.glitch.me/camel/rafaro128@gmail.com"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.text
    else:
        content = f"A solicitação falhou com o código de status {response.status_code}"
    
    return content
