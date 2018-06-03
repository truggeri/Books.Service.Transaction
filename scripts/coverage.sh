#! /bin/bash

pip install --requirement ./src/BooksServiceTransaction/requirements.txt \
            --requirement ./test/requirements.txt \
            coverage
cd test/BooksServiceTransactionTests && coverage run -m pytest
coverage report | grep 'src/BooksServiceTransaction/'