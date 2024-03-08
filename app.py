# file app.py

from flask import Flask, jsonify, send_from_directory
from itertools import repeat
import json
import os                                                                                                               

app = Flask(__name__)

@app.route('/')
def index():

    with open('veepee_prices.json', 'r') as fp:
        final_json = json.load(fp)


    return final_json


if __name__ == '__main__':
    app.run(debug=True,port = 8088)
~     
