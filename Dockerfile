FROM python:3.7.3-slim
COPY requirements.txt /
RUN pip3 install --no-deps -r /requirements.txt
COPY . /app
WORKDIR /app
RUN chmod +x /app/*
ENTRYPOINT ["./gunicorn_runner.sh"]

