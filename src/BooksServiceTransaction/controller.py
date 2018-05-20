from BooksServiceTransaction import app

@app.route("/ok")
def Ok():
    return "ok\n", 200
