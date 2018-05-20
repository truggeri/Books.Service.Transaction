#! /bin/bash

cd src
pip wheel -e .
FLASK_APP=BooksServiceTransaction flask run