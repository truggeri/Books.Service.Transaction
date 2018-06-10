FROM python:3.6
RUN apt-get update -y

COPY ./transaction /app/transaction
COPY ./requirements.txt /app
WORKDIR /app

RUN pip install --requirement requirements.txt

ENTRYPOINT [ "uwsgi", \
    "--http", "0.0.0.0:5000", \
    "-s", "/tmp/transaction.sock", \
    "--manage-script-name", \
    "--mount", "/=transaction:FLASKAPP", \
    "--enable-threads" ]