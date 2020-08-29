FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8
COPY . /app

WORKDIR /app

RUN cd /app

RUN pip3 install pipenv && python3 -m pipenv install --system --deploy

