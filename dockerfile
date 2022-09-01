FROM python:3.10.6-alpine3.15

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./shortener/req.txt /app/req.txt

RUN pip install -r /app/req.txt

COPY . .