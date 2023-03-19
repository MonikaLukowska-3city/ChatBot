FROM python:3.9.16

RUN pip install pipenv    

WORKDIR /app
COPY . .
COPY docker.env .env

RUN pipenv install --ignore-pipfile
