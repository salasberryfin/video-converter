import os
from flask import (
        Flask,
        request,
        render_template,
    )

from utils import common


CURRENT_VERSION = "0.0.0"
DEBUG = True
PORT = 5000
SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "debugging_key"
        )

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


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


@app.route("/users", methods=["POST"])
def sign_up():
    """
    Add a new user to interact with the API
    """
    try:
        user = request.json
        # if not user:
    except Exception as exc:
        return common.form_response(
                "Something went wrong while registering your user",
                500,
                None,
                str(exc),
                )

    return f"Received request for user: {user}"


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
