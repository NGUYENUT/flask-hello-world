from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    response = "lolol"
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/about')
def about():
    return 'About'