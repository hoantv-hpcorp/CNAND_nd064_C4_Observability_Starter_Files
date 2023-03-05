from flask import Flask, jsonify
app = Flask(__name__)

tasks = {"tasks":[
        {"name":"task 1", "uri":"/task1"},
        {"name":"task 2", "uri":"/task2"}
    ]}
    
@app.route('/')
def  root():
	"Service root"
    # tasks = {"tasks": [{"name":"task 1", "uri":"/task1"},{"name":"task 2", "uri":"/task2"}]}
	return jsonify({"url":"/tasks"})
                     
@app.route('/tasks')
def  tasks():
	"Tasks list"
	return  jsonify(tasks)

if __name__ == '__main__':
  "Start up"
  app.run(debug=True, host='0.0.0.0',port=5000)