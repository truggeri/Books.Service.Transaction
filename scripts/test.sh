#! /bin/bash

pip install --requirement ./requirements.txt
cd test && pytest --verbose
