from flask import (
        Flask,
        request,
        render_template,
    )
# from flask_jwt import JWT

from flaskapplication import app, db
from flaskapplication.models import User
from flaskapplication.utils import common
from flaskapplication.security import (
        login_required,
        )


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
            "healthy": True,
            }


@app.route("/users/login", methods=["POST"])
def login():
    """
    Login as registered user
    """
    return "Login path"


@app.route("/users/list", methods=["POST"])
@login_required
def users():
    print("something")
    return "users"


@app.route("/user", methods=["POST"])
def sign_up():
    """
    Add a new user to interact with the API
    """
    required = ["username", "email"]
    try:
        user_data = request.json
        if user_data is not None:
            if any(k not in user_data.keys() for k in required):
                message = "Failed to parse given values"
                error = f"Wrong value. Be sure to provide {required}"

                return common.form_response(
                        msg=message, code=400, err=error,
                    )

            user = User(
                    username=user_data.get("username"),
                    email=user_data.get("email"),
                    )
            user.set_password("mypassword")
            db.session.add(user)
            db.session.commit()
            message = f"User {user.username}:{user.email} was created"

            return common.form_response(
                    msg=message, code=200,
                    )

        message = "Empty request received"
        error = "Request does not contain information"

        return common.form_response(
                    msg=message, code=400, err=error,
                )

    except Exception as exc:
        return common.form_response(
                "Something went server side wrong while registering your user",
                500,
                None,
                str(exc),
                )
