FROM python:3.8.2-slim
# FROM python:3.8.2-buster

RUN mkdir -p /app

WORKDIR /app
COPY main.py /app/main.py

EXPOSE 8080

CMD python3 main.py
