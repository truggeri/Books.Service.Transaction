#! /bin/bash

cd src
pip wheel --verbose --build ./obj --wheel-dir ./bin --editable .