from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the page"

from controller import product_controller, user_controller