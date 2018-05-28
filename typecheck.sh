#! /bin/bash

pip install mypy
mypy --verbose --ignore-missing-imports ./src/BooksServiceTransaction/*.py