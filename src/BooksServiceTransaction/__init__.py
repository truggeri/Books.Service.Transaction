import BooksServiceTransaction.Controllers as controllers
from flask import Flask

app = Flask(__name__)
controllers.HealthController.register(app, route_base='/')