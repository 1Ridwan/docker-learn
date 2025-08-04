# app.py

from flask import Flask
import redis
import os

redis_host=os.getenv('REDIS_HOST', 'redis')
redis_port=int(os.getenv('REDIS_PORT', 6379))

app = Flask(__name__)
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/count')
def homepage():
    # Increment the counter in Redis
    sitevisits = r.incr('visit_count')
    return f'This page has been visited {sitevisits} times!'

@app.route('/')
def hello_world():
    return f'Hello, World! Welcome to my Web app where you will be able to see how many times someone visits the website.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)