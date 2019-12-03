#!/bin/bash

./manage.py migrate  --no-input --traceback
./manage.py collectstatic --no-input --traceback
./manage.py runserver 0.0.0.0:8000

