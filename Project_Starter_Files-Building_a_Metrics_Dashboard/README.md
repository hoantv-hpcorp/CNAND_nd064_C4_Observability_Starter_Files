**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

![Resources Part1](answer-img/TODO1_resource_1.png?raw=true "Resources Part1")

![Resources Part2](answer-img/TODO1_resource_2.png?raw=true "Resources Part2")

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

![Grafana Homepage](answer-img/TODO2_grafana_landing_page.png?raw=true "Grafana Homepage")

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

![Basic dashboard](answer-img/TODO3_basic_dashboard.png?raw=true "Basic dashboard")

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

![Service dashboard](answer-img/TODO6_service_dashboard.png?raw=true "Service dashboard")

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

![Route tracing](answer-img/TODO7_jaeger_trace_span.png?raw=true "Route tracing")

```
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
```

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

![Jeager grafana dashboard](answer-img/TODO8_jaeger_grafana_dashboard.png?raw=true "Jeager grafana dashboard")

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:
System error found in FrontEnd module

Date:
March 6 2023, 15:19:55.935

Subject:
Servere error happens when user call FrontEnd. Do investigate and solve the issue asap

Affected Area:
Error found at FrontEnd Api but it called multiple other services. Do find the root cause and fix other services if needed

Severity:
CRITICAL

Description:
Trace ID: 561abad40bf4ab89
See the picture above for tracing span

![Error tracing](answer-img/TODO9_error_tracing.png?raw=true "Error tracing")


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
