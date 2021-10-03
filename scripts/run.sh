#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

gunicorn bilim.wsgi:application --bind 0.0.0.0:8000 --reload -w 4
