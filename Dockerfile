FROM python:3.7

# Install Requirements
COPY requirements.txt /
RUN pip3 install --no-deps -r /requirements.txt

# Install node/npm
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Copy requirement libraries to app directory
COPY . /app

# Build front-end assets
WORKDIR /app/wombeats-client
RUN npm install
RUN npx browserslist@latest --update-db
RUN npm run build

# Copy compiled front-end assets to app directory
WORKDIR .
RUN mkdir /app/wombeats/static
RUN mv /app/wombeats-client/build/* /app/wombeats/static/

# Do some magic to make it work
RUN chmod +x /app/*
WORKDIR /app
EXPOSE 8080

# Start gunicorn
ENTRYPOINT ["./gunicorn_runner.sh"]
