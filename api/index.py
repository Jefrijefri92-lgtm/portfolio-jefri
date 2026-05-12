from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>WEB JEFRI UDAH LIVE BRO!</h1><p>4 Jam 45 Menit Drama Tamat</p>'

app = app
