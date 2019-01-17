FROM python:3.7.2-alpine3.7

WORKDIR /usr/src/menu

RUN apk add gcc postgresql-dev musl-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
