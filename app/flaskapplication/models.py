from werkzeug.security import (
        generate_password_hash,
        check_password_hash,
    )
from flaskapplication import db


class User(db.Model):
    """
    User defines the elements that define a user when logging in
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    hash = db.Column(db.String())

    def set_password(self, password: str):
        """
        Generate a hash to be stored in the DB from a given password
        """
        self.hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        Given a password return True if correct
        """
        return check_password_hash(self.hash, password)
