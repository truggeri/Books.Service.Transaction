from flask_classful import FlaskView, route

class Transaction(FlaskView):

    @route("/", methods=['POST'])
    def post(self):
        return ("ok", 200)