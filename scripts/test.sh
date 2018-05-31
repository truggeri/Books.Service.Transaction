#! /bin/bash

pip install --requirement ./src/BooksServiceTransaction/requirements.txt pytest
cd test/BooksServiceTransactionTests && pytest --verbose