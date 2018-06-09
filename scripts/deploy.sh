#! /bin/bash

uwsgi --http 0.0.0.0:5000 -s /tmp/transaction.sock --manage-script-name --mount /=transaction:FLASKAPP --enable-threads
