#! /bin/bash

rm -rf transaction/__pycache__
rm -rf transaction/*/__pycache__

rm -rf tests/.pytest_cache
rm -rf tests/__pycache__
rm -rf .pytest_cache

rm -rf ./bin
rm -rf ./build
rm -rf ./obj
rm -rf ./*.egg-info

rm -rf .mypy_cache

rm -rf tests/.coverage