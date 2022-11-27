import os
import logging

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import TestConfig

logger = logging.getLogger("flask_application")
ch = logging.StreamHandler()
formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)

# Flask documentation discourages from setting DEBUG from a config class
# I use this for debugging only
if TestConfig.DEBUG:
    os.environ["FLASK_DEBUG"] = "True"
    logger.setLevel(logging.DEBUG)

logger.info("Retrieving configuration and initializing API")

app = Flask(__name__)
app.config.from_object(TestConfig)
db = SQLAlchemy()
db.init_app(app)


# import all files that contain Flask routable methods
import flaskapplication.views
