from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><h3>Ahoj</h3></html>'