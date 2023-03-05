FROM python:3.8.2-alpine

RUN pip3 install --upgrade pip 
RUN pip3 install --no-cache-dir Flask flask_prometheus_metrics Flask-Opentracing jaeger-client

COPY . /

EXPOSE 5000

CMD ["python", "app.py"]
