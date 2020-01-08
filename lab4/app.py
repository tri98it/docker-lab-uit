import socket
from flask import Flask, request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Test {} hits.\nHostname is {}.\n'.format(count, socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
