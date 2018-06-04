from flask import Flask

from .controllers import health, transaction

app = Flask(__name__)

health.HealthController.register(app, route_base="/")
transaction.Transaction.register(app, route_base="/transaction/")