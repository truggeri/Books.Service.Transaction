#! /bin/bash

pip install --requirement ./src/BooksServiceTransaction/requirements.txt mypy
mypy --verbose --ignore-missing-imports --show-error-context ./src/BooksServiceTransaction/*.py