""" Transaction controller
    Endpoint for /transaction Rest API
"""

from flask_classful import FlaskView, route

from transaction import dependency_manager

class Transaction(FlaskView):

    def __init__(self):
        self._data_store = dependency_manager.data_store

    @route("/", methods=["POST"])
    def post(self):
        self._data_store.create()
        return ("ok", 200)
