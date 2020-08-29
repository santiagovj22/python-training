#FROM python:alpine

FROM jfloff/alpine-python

COPY . /app

WORKDIR /app

RUN cd /app

RUN pip3 install pipenv && python3 -m pipenv install --system --deploy && pip3 install waitress

CMD ["waitress-serve", "--port=8081", "app:app"]
