from flask import Flask
import os
import requests

from prometheus_flask_exporter import PrometheusMetrics

from jaeger_client import Config
from flask_opentracing import FlaskTracing
import opentracing
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0')

config = Config(
    config={
        'sampler':
        {'type': 'const',
         'param': 1},
                        'logging': True,
                        'reporter_batch_size': 1,}, 
                        service_name="frontend")
jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer, True, app)

def get_counter(counter_endpoint):
    counter_response = requests.get(counter_endpoint)
    return counter_response.text

@app.route('/')
def book_ticket():
    parent_span = tracing.get_span()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    parent_span.set_tag("http.timestamp", current_time)

    with opentracing.tracer.start_span('backend-api', child_of=parent_span) as span:
        counter_service = os.environ.get('COUNTER_ENDPOINT', default="https://localhost:5000")
        span.set_tag("http.url", counter_service)
        counter_endpoint = f'{counter_service}/get-ticket'
        counter = get_counter(counter_endpoint)
        span.set_tag("http.counter", counter)

    return f"""Your number is {counter}! \n"""

@app.route('/simulate_system_error')
def simulate_system_error():
    parent_span = tracing.get_span()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    parent_span.set_tag("http.timestamp", current_time)

    with opentracing.tracer.start_span('backend-api', child_of=parent_span) as span:
        counter_service = os.environ.get('COUNTER_ENDPOINT', default="https://localhost:5000")
        span.set_tag("http.url", counter_service)
        counter_endpoint = f'{counter_service}/get-ticket'
        counter = get_counter(counter_endpoint)
        span.set_tag("http.counter", counter)

    with opentracing.tracer.start_span('post-api', child_of=parent_span) as span:
        counter_service = os.environ.get('COUNTER_ENDPOINT', default="https://localhost:5000")
        span.set_tag("http.url", counter_service)
        counter_endpoint = f'{counter_service}/system-error'
        result = get_counter(counter_endpoint)
        span.set_tag("http.counter", counter)

    # Simulate a system error occurs 
    1/0
    return "Should not reach here"
