#! /bin/bash

cd tests && coverage run -m pytest
coverage report | grep '/transaction/'