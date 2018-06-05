""" Transaction controller
    Endpoint for /transaction Rest API
"""

from flask_classful import FlaskView, route

from transaction.storage import database

class Transaction(FlaskView):

    def __init__(self):
        pass

    @route("/", methods=["POST"])
    def post(self):
        database.create()
        return ("ok", 200)
