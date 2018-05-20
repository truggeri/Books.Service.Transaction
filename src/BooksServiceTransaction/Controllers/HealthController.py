from BooksServiceTransaction import app
from flask import request
import flask

@app.route("/ok")
def Ok():
    return "ok\n", 200

@app.route("/health")
def Health():
    result = {'healthy' : True}
    return (flask.jsonify(result), 200)