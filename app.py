from flask import Flask
import redis
import os

app = Flask(__name__)


@app.route('/')
def index():
    username = os.environ.get('REDIS_USERNAME')
    password = os.environ['REDIS_PASSWORD']
    host = os.environ['REDIS_HOST']
    port = os.environ['REDIS_PORT']
    db = os.environ['REDIS_DB']
    client = redis.Redis(username=username, password=password,
                         host=host, port=port, db=db)
    key = 'HIT_COUNT'
    value = client.get(key)
    """ Original line: count = int(client.get(key)) or 0
     Problem with this is since we are not connecting to a live redis DB, an error will occur because the client.get(key) method returns None when the key doesn't exist in Redis. 
     When you try to convert None to an integer using int(), it raises a TypeError. 
     To resolve this we should check if the key exists in Redis before trying to convert it to an integer. 
     If the key doesn't exist, this now defaults to 0. """
    count = int(value) if value is not None else 0
    response = f'Hello FELFEL. The count is: {count}'
    client.set(key, count + 1)

    return response


app.run(host='0.0.0.0', port=8080)
