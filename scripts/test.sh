#! /bin/bash

pip install --requirement ./requirements.txt
cd test/BooksServiceTransactionTests && pytest --verbose
