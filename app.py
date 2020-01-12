from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init App

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'msg': 'Hello Techyowls!'})


# Run Server

if __name__ == '__main__':
    app.run(debug=True)
