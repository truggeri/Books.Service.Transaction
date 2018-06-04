#! /bin/bash

pip install --requirement ./requirements.txt
cd test && coverage run -m pytest
coverage report | grep 'src/BooksServiceTransaction/'
