#! /bin/bash

cd src
pip wheel --quiet --build ./obj --wheel-dir ./bin --editable .
FLASK_APP=BooksServiceTransaction flask run