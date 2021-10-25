FROM python:3.8

RUN pip install numpy

RUN apt-get update && apt-get install -y supervisor

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY . /app

WORKDIR /app

RUN mkdir monitoring

CMD [ "/usr/bin/supervisord" ]