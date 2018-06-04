import json

from flask_classful import FlaskView, route
from typing import Tuple

class HealthController(FlaskView):
    """A class of health related endpoints"""

    @route("ok", methods=["GET"])
    def ok(self) -> Tuple[str, int]:
        return ("ok", 200)

    @route("health", methods=["GET"])
    def health(self):
        result = {"Healthy" : True}
        return (json.dumps(result, indent=4), 200)