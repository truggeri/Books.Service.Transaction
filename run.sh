#! /bin/bash

cd src/Books.Service.Transaction
pip install -r requirements.txt
FLASK_APP=main.py flask run