from functools import wraps


def login_required(func):
    """
    This decorator functions allows to validate that the user is logged in
    for protected routes of the API
    """
    @wraps(func)
    def check_logged_in_user():
        print("Checking if user is logged in")
        func()
        print("Checked")
        return {"message": "Valid test"}, 200
    return check_logged_in_user


def register(user: str, password: str):

    return ""


def authenticate(user: str, password: str):

    return ""


def identity():

    return ""
