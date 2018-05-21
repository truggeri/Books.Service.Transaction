FROM python:3.6
RUN apt-get update -y

COPY ./src /app
WORKDIR /app

RUN pip install --requirement ./BooksServiceTransaction/requirements.txt

ENV FLASK_APP=BooksServiceTransaction
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]