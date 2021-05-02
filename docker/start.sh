#!/bin/bash

while ! (timeout 3 bash -c "</dev/tcp/${POSTGRES_HOST}/${POSTGRES_PORT}") &> /dev/null;
do
  echo waiting for PostgreSQL to start...;
  sleep 3;
done;

./manage.py migrate  --no-input --traceback
./manage.py collectstatic --no-input --traceback
./manage.py runserver 0.0.0.0:8000

