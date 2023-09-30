#  Import what we need from flask
from flask import Flask

# Create a Flask app inside 'app'
app = Flask(__name__)

# Assign a function to be called when the path '/' is requested
@app.route('/')
def index():
        return 'Hello, WINC Teacher!!'

@app.route('/cow')
def cow():
        return 'The cow says Moooooow!'

if __name__ ==  "__main__":
        app.run(debug=True)