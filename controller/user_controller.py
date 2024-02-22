from app import app
from model.user_model import UserModel

@app.route("/user/signup")
def user_signup_controller():
    # Path Controller
    return UserModel().user_signup_model()