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

Since SLO is the expected performance of the system, SLIs are the actual measurement of *monthly uptime* and *request response time*. For example, at the end of the month, we observe that the total uptime in month is 99.9% and 99% of request response time is under 500ms.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

Below are 5 metrics we may use to measure our system:
- Total node/pod uptime in month
- CPU usage
- Memory usage
- Average request response time
- Maximum request response time

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

In order to achive SLO, we are going to monitoring these values:
- CPU usage
- Memory usage
- Total request rate
- Request response time

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

The metrics are listed below; 
- CPU usage
  - Maximum CPU usage should be 70%. We need this to ensure that the system preseve enough computing resource to serve incoming request
- Memory usage
  -  Memory consumption of each service should be less than 256MB. This metrics indices that system can handle incoming request within allocated memory
- Total request rate
  - Request rate limit is 100 req/s. We have this metrics to make sure that one request will not have to wait to long in queue and also that the application have enough thread to process multiple request simultainiously
- Request response time
  - Average response time is 500ms. This metrics indicate that in general most of the requests will be served fast enough.
  - Maximum request response time is 1s. We need to ensure that, even in the worst case, the clients don't have to wait to long to get the result

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

![Final dashboard 1](answer-img/TODO10_final_dashboard1.png?raw=true "Final dashboard 1")
![Final dashboard 2](answer-img/TODO10_final_dashboard2.png?raw=true "Final dashboard 2")

- *CPU Usage*: describe percentage of CPU usage for each service
- *Process memory*: describe how much memory a service consumes
- *Avegrage request response time*: describe in average how long a service need to handle the incoming requests 
- *Total request rate*: mesure how many request were handled at a period of time
- *System Error Requests*: a table listing Jaeger trace of the request which return 500 System Error. This will help to investigate the issue later
- *Pod uptime*: measure how long the kubernetes pod is up to serve incoming requests
- *40x and 50x error count*: this graphs summary the errornous request in our system.
- *40x and 50x error count*: this one has similar purpose with previous graph. However by looking in to this graph we have an ideal of when and how many errornous requests are observed.  