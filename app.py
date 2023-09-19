from flask import Flask, Response
import redis
import os
from prometheus_client import start_http_server, Counter, generate_latest

app = Flask(__name__)

# Creates a counter metric
HIT_COUNTS = Counter('hit_count', 'Number of hits')


@app.route('/')
def index():
    username = os.environ.get('REDIS_USERNAME')
    password = os.environ['REDIS_PASSWORD', 'default_password']
    host = os.environ['REDIS_HOST']
    port = os.environ['REDIS_PORT']
    db = os.environ['REDIS_DB']
    client = redis.Redis(username=username, password=password,
                         host=host, port=port, db=db)
    key = 'HIT_COUNT'
    value = client.get(key)
    """ Original line: count = int(client.get(key)) or 0
     An error will occur here because the client.get(key) method returns None when the key doesn't exist in Redis. 
     When you try to convert None to an integer using int(), it raises a TypeError. 
     To resolve this we should check if the key exists in Redis before trying to convert it to an integer. 
     If the key doesn't exist, this now defaults to 0. """
    count = int(value) if value is not None else 0

    # Increment the Prometheus counter
    HIT_COUNTS.inc()

    response = f'Hello FELFEL. The count is: {count}'
    # every time we refresh the browser, count increases by 1
    client.set(key, count + 1)

    return response


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')


if __name__ == '__main__':
    # Start the Prometheus client
    start_http_server(9090)
    app.run(host='0.0.0.0', port=8080)
