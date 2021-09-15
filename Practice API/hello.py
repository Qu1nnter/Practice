from flask import Flask, jsonify
from random import randint

app = Flask(__name__)

@app.route("/")
def hello_world():
    a= randint(1, 100)
    output= {
        "Important Message": "Ooga Booga",
        "randint": a,
        "arr": [
        {"Name": "Kam", "Age": 23, "Major": "Aerospace Engineering"}, 
        {"Name": "Bammy", "Age": 27, "Major": "Computer Science"}, 
        {"Name": "Samuel", "Age": 87, "Major": "Civil Engineering"}
        ]
    }
    return jsonify(output)



#export FLASK_APP=hello.py
#flask run
#^To run test server^