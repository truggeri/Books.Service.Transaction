#! /bin/bash

pip install --requirement ./requirements.txt
pytest --verbose tests
