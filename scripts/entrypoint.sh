# !/bin/bash
python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --noinput

#python manage.py runserver 0.0.0.0:8000

#gunicorn --bind=0.0.0.0:8000 --workers=8 bilim.wsgi

gunicorn bilim.wsgi:application --bind 0.0.0.0:8000 --reload -w 4

