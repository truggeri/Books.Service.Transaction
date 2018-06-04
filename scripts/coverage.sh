#! /bin/bash

pip install --requirement ./requirements.txt
cd tests && coverage run -m pytest
coverage report | grep '/transaction/'