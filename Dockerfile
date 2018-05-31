FROM python:3.6
RUN apt-get update -y

COPY ./src /app
WORKDIR /app

RUN pip install --requirement ./BooksServiceTransaction/requirements.txt uwsgi

ENV FLASK_APP=BooksServiceTransaction
ENTRYPOINT [ "uwsgi", "--http", "0.0.0.0:5000", "--module", "BooksServiceTransaction:app", "--enable-threads" ]