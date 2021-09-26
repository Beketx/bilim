#!/bin/sh

sudo python manage.py makemigrations

sudo python manage.py migrate

sudo python manage.py collectstatic --noinput

#sudo python manage.py runserver 0.0.0.0:8000

gunicorn bilim.wsgi:application --bind 0.0.0.0:8000 --preload -w 4

