#! /bin/bash

pip install --requirement ./requirements.txt
cd src && FLASK_APP=BooksServiceTransaction flask run
