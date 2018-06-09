""" Package for Books.Service.Transaction service.
    Provides web api for transactions in the Book app.
"""

from flask import Flask

from .controllers import health, transaction
from . import config

FLASKAPP = Flask(__name__)

health.HealthController.register(FLASKAPP, route_base="/")
transaction.Transaction.register(FLASKAPP, route_base="/transaction/")
