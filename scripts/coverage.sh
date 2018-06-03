#! /bin/bash

pip install --requirement ./src/BooksServiceTransaction/requirements.txt pytest coverage
cd test/BooksServiceTransactionTests && coverage run -m pytest
coverage report | grep 'src/BooksServiceTransaction/'