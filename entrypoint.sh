#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear

gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 4
