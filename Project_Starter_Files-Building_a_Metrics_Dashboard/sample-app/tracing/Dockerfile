FROM python:3.8.2-alpine

RUN pip3 install --upgrade pip 
RUN pip3 install --no-cache-dir Flask requests prometheus-flask-exporter Flask-Opentracing jaeger-client

COPY . /

ENV FLASK_APP frontend.py

CMD flask run --host=0.0.0.0 --port=8000