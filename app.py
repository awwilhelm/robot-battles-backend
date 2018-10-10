#!flask/bin/python
from flask import Flask, request, Response, session, jsonify
from json import dumps, loads, JSONEncoder, JSONDecoder
import pickle
from ReturnObjects import Student

def returnThis(message, status, result):
    return jsonify(message=message, status=status, result=result)

app = Flask(__name__)

@app.route('/')
def index():
    return returnThis('success', 200, Student("one", 2, "three").__dict__)

@app.route('/api/move', methods=['POST'])
def move():
    json_data = request.json
    if('distance' not in json_data or 'angle' not in json_data):
        return returnThis('Not sending correct parameters', 400, None)
    if(not isinstance(json_data['distance'], float) or not isinstance(json_data['angle'], float)):
        return returnThis('Parameters are not correct input type', 400, None)

    
    return returnThis('success', 200, json_data)
  

if __name__ == '__main__':
    app.run(debug=True)


