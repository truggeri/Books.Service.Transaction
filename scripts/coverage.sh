#! /bin/bash

pip install --requirement ./requirements.txt
cd test/BooksServiceTransactionTests && coverage run -m pytest
coverage report | grep 'src/BooksServiceTransaction/'
