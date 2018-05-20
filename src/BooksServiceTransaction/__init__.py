from flask import Flask
app = Flask(__name__)

from BooksServiceTransaction.Controllers.HealthController import *
HealthController.register(app, route_base='/')