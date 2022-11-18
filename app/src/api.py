import os
from flask import (
        Flask,
        request,
        render_template,
    )
# from flask_jwt import JWT

from models import db, User
from utils import common
# from security import authenticate, identity


CURRENT_VERSION = "0.0.0"
DEBUG = True
PORT = 5000
DB_NAME = "localtest.db"
SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "debugging_key"
        )

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

db.init_app(app)


@app.before_first_request
def init_db():
    """
    Before anything happens, create the DB tables
    """
    with app.app_context():
        db.create_all()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/health", methods=["GET"])
def health():
    return {
            "API Version": CURRENT_VERSION,
            }


@app.route("/users/login", methods=["POST"])
def login():
    """
    Login as registered user
    """
    return "Login path"


@app.route("/check", methods=["GET"])
def check():
    user = User(
            email="salasberryfin@email.com",
            username="salasberryfin",
            )
    user.set_password("mypassword")
    db.session.add(user)
    db.session.commit()

    return common.form_response(
            f"Setting password as {user.hash}",
            200,
            f"Checking for user {user.username} with email {user.email}",
            None,
            )


@app.route("/user", methods=["POST"])
def sign_up():
    """
    Add a new user to interact with the API
    """
    message = ""
    status_code = 200
    data = None
    error = None
    # required parameters: username, email, password
    required = ["username", "email"]
    try:
        user_data = request.json
        if user_data is not None:
            if any(k not in user_data.keys() for k in required):
                message = "Failed to parse given values"
                error = f"Wrong value. Be sure to provide {required}"
                return common.form_response(
                        msg=message, code=status_code, data=data, err=error,
                    )
        else:
            message = "Empty request received"
            status_code = 400
            error = "Request does not contain information"
            return common.form_response(
                        msg=message, code=status_code, data=data, err=error,
                    )
    except Exception as exc:
        return common.form_response(
                "Something went wrong while registering your user",
                500,
                None,
                str(exc),
                )

    return common.form_response(
                msg=message, code=status_code, data=data, err=error,
            )


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
