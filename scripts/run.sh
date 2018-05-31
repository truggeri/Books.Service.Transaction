#! /bin/bash

pip install --requirement ./src/BooksServiceTransaction/requirements.txt
cd src && FLASK_APP=BooksServiceTransaction flask run