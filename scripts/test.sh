#! /bin/bash

pip install --requirement ./src/BooksServiceTransaction/requirements.txt \
            --requirement ./test/requirements.txt
cd test/BooksServiceTransactionTests && pytest --verbose