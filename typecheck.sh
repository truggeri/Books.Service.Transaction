#! /bin/bash

pip install mypy
mypy --verbose --ignore-missing-imports --show-error-context ./src/BooksServiceTransaction/*.py