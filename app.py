from flask import Flask, request

app = Flask(__name__)


@app.get('/')
def helloGet():
    return 'Hello world GET'


@app.post('/')
def helloPost():
    return 'Hello world POST:{}'.format(request.data)


if __name__ == '__main__':
    app.run(port=8080)
