""" Package for Books.Service.Transaction service.
    Provides web api for transactions in the Book app.
"""

from flask import Flask

from transaction.controllers.health import HealthController
from transaction.controllers.transaction import TransactionController
from . import config

FLASKAPP = Flask(__name__)

HealthController.register(FLASKAPP, route_base="/")
TransactionController.register(FLASKAPP, route_base="/transaction/")
