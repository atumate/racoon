#!/usr/bin/env python
from flask import Flask

import response

app = Flask(__name__)

@app.route('/')
def index():
    jsonStr=response.raw_response("http://nixni.cc")
    return jsonStr


@app.route('/about')
def about():
    return 'The about page'











if __name__ == '__main__':
    app.run(debug=True)