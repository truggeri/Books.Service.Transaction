FROM python:3.6
RUN apt-get update -y

COPY ./requirements.txt /app/
WORKDIR /app

RUN pip install --requirement requirements.txt

ENV FLASK_APP=transaction
ENV FLASK_ENV=development
ENV FLASK_DEBUG=false

EXPOSE 5000
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]