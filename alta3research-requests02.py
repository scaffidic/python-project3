#!/usr/bin/env python3

import json
import requests
from pprint import pprint


# API url to alta3research-flask01.py
apiURL = "http://127.0.0.1:2224/"

# new list item to post
new_sde = {
    "company": "Goole",
    "position": "software engineer",
    "state": "Washington",
    "city": "Seattle",
    "firstName": "Billy",
    "lastName": "Smith",
    "age": 33,
    "experience": "SDE 1"

}

new_sde = json.dumps(new_sde)

resp = requests.post(apiURL, json=new_sde)

pprint(resp.json())
