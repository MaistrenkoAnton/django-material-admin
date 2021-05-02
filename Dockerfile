FROM python:3.8
MAINTAINER Anton Maistrenko

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /app
RUN mkdir /app/material

WORKDIR /app
COPY ./app /app
COPY ./material /app/material
COPY ./docker /app/docker
COPY ./tests /app/test

RUN chmod +x /app/docker/start.sh

CMD ["/app/docker/start.sh"]