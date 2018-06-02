#!/usr/bin/env python
from flask import Flask, send_from_directory

import response

app = Flask(__name__)

# @app.route('/')
# def index():
#     jsonStr=response.raw_response("http://nixni.cc")
#     return jsonStr


# @app.route('/about')
# def about():
#     return 'The about page'


@app.route('/i')
def index2():
    return 'aha'

@app.route('/')
def index():
    return send_static('index.html')    


@app.route('/<path:filename>')
def send_static(filename):
    return send_from_directory('static',
                               filename)

# @app.route('/<path:filename>')
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename, as_attachment=True)









if __name__ == '__main__':
    app.run(debug=True)