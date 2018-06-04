#! /bin/bash

pip install --requirement ./requirements.txt
FLASK_APP=transaction/__init__.py flask run
