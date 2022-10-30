
# A very simple Flask Hello World app for you to get started with...

from flask import Response
from flask import Flask
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {"slackUsername": "Okor Mark", "backend": True, "age": 20, "bio": "My name is Okor Mark and i am an aspiring backend engineer"}
    json_dump = json.dumps(data_set)
    return Response(json_dump, mimetype='application/json')
