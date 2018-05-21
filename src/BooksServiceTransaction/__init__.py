from BooksServiceTransaction.Controllers import *
from flask import Flask

app = Flask(__name__)
HealthController.register(app, route_base='/')