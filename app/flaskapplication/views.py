import logging
from flask import (
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


logger = logging.getLogger("flask_application")


@app.before_first_request
def init_db():
    """
    Before anything happens, create the DB tables
    """
    with app.app_context():
        db.create_all()


@app.route("/")
def home():
    logger.debug("Home requested")
    return render_template("home.html")


@app.route("/admin")
@login_required
def admin():
    logger.debug("Admin only resource")
    return "Admin user"


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
    try:
        username = request.form.get("username")
        password = request.form.get("password")
        assert username is not None
        assert password is not None
    except AssertionError as err:
        return common.form_response(
                "Your request is missing data: check username and password",
                400,
                None,
                str(err),
                )

    user_from_db = User.query.filter_by(username=username).first()

    if not user_from_db.check_password(password):
        message = f"Failed to login as {user_from_db.username}"
        status_code = 403
        error = "Incorrect username or password"
    else:
        message = f"Successfully logged in as {user_from_db.username}"
        status_code = 200
        error = None

    return common.form_response(
            message,
            status_code,
            None,
            error,
            )


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
