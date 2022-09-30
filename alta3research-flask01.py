#!/usr/bin/env python3

"""Project 3 - Using Flask API's"""


from crypt import methods
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import json


# Start API
app = Flask(__name__)

# Python list containing a dictonary with information about an employee
amazon_sde = [{
    "company": "Amazon",
    "position": "software engineer",
    "state": "New York",
    "city": "NYC",
    "firstName": "Christian",
    "lastName": "Scaffidi",
    "age": 25,
    "experience": "apprentice"

}]


# First endpoint/ route "home"
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        data = request.json
        if data:
            data = json.loads(data)
            company = data["company"]
            position = data["position"]
            state = data["state"]
            city = data["city"]
            firstName = data["firstName"]
            lastName = data["lastName"]
            age = data["age"]
            experience = data["experience"]
            amazon_sde.append({"company": company, "position": position, "state": state, "city": city,
                              "firstName": firstName, "lastName": lastName, "age": age, "experience": experience})

    return jsonify(amazon_sde)


# Second endpoint/ route. Takes you to index.html "welcome screen"
@app.route("/<username>")
def index(username):
    return render_template("index.html", name=username)


# Third endpoint where user gets "Rick Rolled"
@app.route("/<username>/roll")
def roll(username):
    return render_template("roll.html", name=username)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2224)
