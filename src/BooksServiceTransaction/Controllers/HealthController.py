from BooksServiceTransaction import app
from flask import jsonify, request

@app.route("/ok")
def Ok():
    return "ok\n", 200

@app.route("/health")
def Health():
    result = {'healthy' : True}
    return (jsonify(result), 200)