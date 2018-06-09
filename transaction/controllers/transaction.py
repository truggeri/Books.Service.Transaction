""" Transaction controller
    Endpoint for /transaction Rest API
"""

from flask_classful import FlaskView, route

from transaction.storage.database import Database

class Transaction(FlaskView):

    def __init__(self):
        pass

    @route("/", methods=["POST"])
    def post(self):
        Database("blank", "password1234")
        return ("ok", 200)
