""" Transaction controller
    Endpoint for /transaction Rest API
"""

from flask_classful import FlaskView, route

class TransactionController(FlaskView):

    def __init__(self):
        pass

    @route("/", methods=["POST"])
    def post(self):
        return ("ok", 200)
