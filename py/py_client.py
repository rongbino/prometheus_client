from prometheus_client import start_http_server, Summary
import random
import time

# create a metrix to track time spent and requests made
REQUEST_TIME = Summary('py_request_processing_seconds', 'Time spent processing request')

# Decorate functionwith metric
@REQUEST_TIME.time()
def process_request(t):
    """ A dump function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics
    start_http_server(9090)
    # Genrrate some requests
    while True:
        process_request(random.random())
