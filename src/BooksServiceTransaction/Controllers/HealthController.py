from flask import jsonify
from flask_classful import FlaskView, route

class HealthController(FlaskView):
    """A class of health related endpoints"""

    @route("ok")
    def Ok(self):
        return ("ok", 200)

    @route("health")
    def Health(self):
        result = {'healthy' : True}
        return (jsonify(result), 200)