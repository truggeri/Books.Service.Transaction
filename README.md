# Books.Service.Transaction

Service for transactions in the Books project.

[![Build Status](https://travis-ci.org/truggeri/Books.Service.Transaction.svg?branch=master)](https://travis-ci.org/truggeri/Books.Service.Transaction)
[![Coverage Status](https://coveralls.io/repos/github/truggeri/Books.Service.Transaction/badge.svg?branch=master)](https://coveralls.io/github/truggeri/Books.Service.Transaction?branch=master)

This service is intended to be the source of truth for transactions in the Books project. This includes reads and writes, though those may be handled in isolation. This is a python 3 project.

## Running

To run the service,

```bash
./scripts/run.sh
```

This script will start a [flask web server](http://flask.pocoo.org/docs/1.0/deploying/). Note that this is not suitable as a production ready server.

## Using Docker Compose

This project includes a `docker-compose.yml` file for setting up the entire development environment. This will stand up a local CouchDB instance and connect it to the local instance of the service. Note that there are some requirements to setup the database for the first time that are not part of the compose file (documentation @TODO). To use, simple run,

```bash
docker-compose up
```

## Testing

To run unit tests,

```bash
./scripts/test.sh
```

This script will simply call the appropriate python programs to run all unit tests with [pytest](https://docs.pytest.org/en/latest/index.html).

## Type checking

This project is attempting to use the new python type checking. For the time being it is run using [mypy](http://mypy-lang.org/). To run the type checking,

```bash
./scripts/typecheck.sh
```

I found [this PyCon 2018 video](https://www.youtube.com/watch?v=QCGwDOk-pIs) very informative. I don't have any plans to use [Pyre](https://pyre-check.org/) until there is an option to ignore missing imports.