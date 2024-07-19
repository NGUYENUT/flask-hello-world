from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    response = jsonify(message="Simple server is running")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/about')
def about():
    return 'About'