FROM ubuntu
COPY requirements.txt /
RUN pip3 install --no-deps -r /requirements.txt
COPY . /app
WORKDIR /app/wombeats-client
RUN curl --silent --location https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y \
  nodejs
RUN echo "Node: " && node -v
RUN echo "NPM: " && npm -v
WORKDIR /app
RUN chmod +x /app/*
ENTRYPOINT ["./gunicorn_runner.sh"]
