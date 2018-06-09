#!/usr/bin/env python
from flask import Flask, send_from_directory, request
from pprint import pprint
import r_ant
import json
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return send_static('index.html')   


@app.route('/api', methods=['POST', 'GET'])
def api():
    if request.method == 'POST':
        result=r_ant.parse_post_data(request.json);
        return json.dumps(result,indent=4, sort_keys=True)

    else:
        jsonStr=response.raw_response("http://nixni.cc")
        return jsonStr



# static
@app.route('/<path:filename>')
def send_static(filename):
    return send_from_directory('static',
                               filename)
 








if __name__ == '__main__':
    app.run(debug=True)