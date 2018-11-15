from flask import Flask, jsonify
# from pymongo import MongoClient

import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'hello': 'world'})

@app.route('/db')
def database():
    return jsonify({'env': os.environ.get('MONGODB_URI')})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
