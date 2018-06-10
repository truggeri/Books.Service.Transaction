""" Health controller.
    Endpoints for container health checks.
"""

import json

from flask_classful import FlaskView, route
from typing import Tuple

from transaction.storage.database import Database

class HealthController(FlaskView):
    """A class of health related endpoints"""

    @route("ok", methods=["GET"])
    def ok(self) -> Tuple[str, int]:
        return ("ok", 200)

    @route("health", methods=["GET"])
    def health(self) -> Tuple[str, int]:
        result = {"Healthy" : True}
        return (json.dumps(result, indent=4), 200)

    @route("health/db", methods=["GET"])
    def db_health(self) -> Tuple[str, int]:
        client = Database()
        client.connect()
        (result, info) = client.health()
        client.disconnect()
        if not result:
            return (json.dumps({"Healthy": False}), 502)
        return (json.dumps(info, indent=4), 200)
