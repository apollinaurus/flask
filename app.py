from flask import Flask

app = Flask(__name__)

@app.get('/')
def helloGet():
    return 'Hello world GET'

@app.post('/')
def helloPost():
    return 'Hello world POST'