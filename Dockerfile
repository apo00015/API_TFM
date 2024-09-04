FROM python:3.10.4-alpine3.15

WORKDIR /
ADD / /
RUN mkdir -p /var/log/microservices
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apk add --no-cache --virtual .build-deps gcc musl-dev

RUN python -m unittest discover -s tests

CMD gunicorn $GUNICORN_ARGS -t 120 -b :5000 main:app