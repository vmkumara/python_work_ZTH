from flask import Flask  #(from flaak package we import the Flask module)

import requests
from requests.auth import HTTPBasicAuth
import json


#create a flask app instance
app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'])
# def hellow():
#  return "Hellow world"


def createJira():

    url = "https://svenkatamkumara-1721368667466.atlassian.net//rest/api/3/issue"

    API_TOKEN="------------------------------------------------------"
    auth = HTTPBasicAuth("___________________@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "My FirstJIRA Ticket",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "MAN"
        },
        "issuetype": {
            "id": "10008"
        },
        "summary": "FirstJIRA ticket",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


app.run("0.0.0.0", port=5000)

