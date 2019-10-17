FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    netcat

RUN pip install --upgrade pip && pip install pipenv
