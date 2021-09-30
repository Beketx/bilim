FROM python:3.9-slim-buster

LABEL MAINTAINER="Beket Samaluly"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && \
    # Без установки рекомендованных пакетов
    apt-get install -y --no-install-recommends \
    # Для установки RU.UTF-8
    locales \
    # Пакеты для компиляции
    build-essential \
    # Для работы с psycopg2-binary
    libpq-dev

RUN locale-gen en_US ru_RU.UTF-8
COPY requirements.txt /code/

WORKDIR /code

RUN pip3 install --upgrade pip==21.2.4

RUN pip3 install -r requirements.txt

COPY . /code/
