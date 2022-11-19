from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import TestConfig


app = Flask(__name__)
app.config.from_object(TestConfig)
db = SQLAlchemy()
db.init_app(app)


# import all files that contain Flask routable methods
import flaskapplication.views
