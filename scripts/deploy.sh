#! /bin/bash

pip install --requirement ./src/BooksServiceTransaction/requirements.txt uwsgi
cd src/BooksServiceTransaction && uwsgi --http 0.0.0.0:5000 --module BooksServiceTransaction:app --enable-threads