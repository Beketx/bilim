#!/bin/bash

sudo python manage.py makemigrations

sudo python manage.py migrate

sudo python manage.py collectstatic --noinput

sudo python manage.py runserver 0.0.0.0:8000

#gunicorn --bind=0.0.0.0:8000 --workers=8 bilim.wsgi
#
