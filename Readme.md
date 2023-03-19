pip install pipenv

=============
pipenv shell
pip install certifi

python -m spacy info
python -m spacy download pl_core_news_sm

=====================
https://medium.com/analytics-vidhya/create-and-dockerize-a-project-with-rasa-flask-and-mongodb-with-docker-and-docker-compose-75c9c6e3c74b

https://www.analyticsvidhya.com/blog/2022/02/a-simple-guide-to-rasa-3-x/

=====================
Lokalne odpalanie do developmentu

1. Uruchom z docker compose tylko web + baze danych + duckling

2. cd C:\Nauka\chatbot\flask -> pipenv run python app.py

3. cd C:\Nauka\chatbot\rasa_engine -> pipenv run rasa run actions

4. cd C:\Nauka\chatbot\rasa_engine -> pipenv run rasa run --enable-api --cors "\*" --debug

Wejdz na strone localhost i zacznij czat

=====================
Odpalanie całosci z docker:

cd D:\chatbot\rasa_engine
docker build -t rasa_engine .

docker-compose up

=====================
https://rasa.com/docs/rasa/
