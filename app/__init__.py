import logging

from flask import Flask

from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app import routes


gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(logging.INFO)
