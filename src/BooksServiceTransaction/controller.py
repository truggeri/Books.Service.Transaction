from BooksServiceTransaction import app
from flask import request

@app.route("/ok")
def Ok():
    return "ok\n", 200

@app.route("/transaction", methods=['POST'])
def TransactionPost():
    if request.get_json() == None:
        return ("Expected json request body", 400)
    return ("ok\n", 304)