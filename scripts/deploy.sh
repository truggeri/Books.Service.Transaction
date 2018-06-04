#! /bin/bash

pip install --requirement ./requirements.txt
uwsgi --http 0.0.0.0:5000 --module transaction:app --enable-threads
