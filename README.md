# Books.Service.Transaction

Service for transactions in the Books project.

This service is intended to be the source of truth for transactions in the Books project. This includes reads and writes, though those may be handled in isolation. This is a python 3 project.

## Running

To run the service,

```bash
./run.sh
```

This script will start the flask app that hosts the service.

## Using Docker

The included Dockerfile can be used to build a container image that runs this project. To build the image,

```bash
docker build -t books-service-transaction:latest .
```

And then to start the container,

```bash
docker run -p 5000:5000/tcp --name books-transaction books-service-transaction
```

## Testing

To run unit tests,

```bash
./test.sh
```

This script will simply call the appropriate python programs to run all py unittests.

## Type checking

This project is attempting to use the new python type checking. For the time being it is run using [mypy](http://mypy-lang.org/). To run the type checking,

```bash
./typecheck.sh
```

I found [this PyCon 2018 video](https://www.youtube.com/watch?v=QCGwDOk-pIs) very informative. I don't have any plans to use [Pyre](https://pyre-check.org/) until there is an option to ignore missing imports.