# Books.Service.Transaction
Service for transactions in the Books project.

This service is intended to be the source of truth for transactions in the Books project. This includes reads and writes, though those may be handled in isolation. This is a python 3 project.

## To run
To run the service, run
```bash
./run.sh
```
This script will start the flask app that hosts the service. Note, this service _should_ also be able to be run via the Dockerfile.

## To test
To run unit tests, run
```bash
./test.sh
```

This script will simply call the appropriate python programs to run all py unittests.