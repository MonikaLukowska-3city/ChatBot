FROM python:3.10-bullseye

RUN apt-get update
RUN apt-get install -y curl

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev mssql-tools


RUN pip3 install --upgrade pip
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc 


RUN pip3 install pipenv
WORKDIR /app
COPY . . 
COPY docker.env .env
RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "python", "app.py" ]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]