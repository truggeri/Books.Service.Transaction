#! /bin/bash

pip install --requirement ./requirements.txt
mypy --verbose --ignore-missing-imports --show-error-context ./transaction/*.py
