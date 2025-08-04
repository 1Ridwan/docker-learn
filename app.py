# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, World! Welcome to my Web app where you will be able to see how many times someone visits the website.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)