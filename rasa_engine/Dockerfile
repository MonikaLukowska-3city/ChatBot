FROM python:3.10-bullseye

RUN pip install pipenv    

WORKDIR /app
COPY . .
COPY docker.env .env

RUN pipenv install --ignore-pipfile
