FROM python:3.7
COPY requirements.txt /
RUN pip3 install --no-deps -r /requirements.txt
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
COPY . /app
WORKDIR /app/wombeats-client
RUN npm install
RUN npx browserslist@latest --update-db
RUN npm run build
RUN mkdir /app/static
RUN mv build/* /app/static/
WORKDIR /app
RUN chmod +x /app/*
EXPOSE 8080
ENTRYPOINT ["./gunicorn_runner.sh"]
