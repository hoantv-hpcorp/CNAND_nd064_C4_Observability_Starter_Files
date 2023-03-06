FROM python:3.8.2-alpine

RUN pip3 install --upgrade pip 
RUN pip3 install --no-cache-dir Flask requests flask_prometheus_metrics Flask-Opentracing jaeger-client

COPY . /

EXPOSE 8000

CMD ["python", "frontend.py"]
