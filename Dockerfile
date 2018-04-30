FROM python:3.6
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY ./src /app
WORKDIR /app/Books.Service.Transaction
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]