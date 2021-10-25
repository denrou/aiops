FROM python:3.8

RUN pip install numpy

RUN apt-get update

COPY . /app

WORKDIR /app

CMD [ "/app/application.py" ]