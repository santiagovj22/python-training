#Use Python 3.7
FROM python:3.7
#PipEnv
RUN pip3 install pipenv

RUN mkdir /api
WORKDIR /api

COPY . /api

RUN cd /api

RUN python3 -m pipenv install --system --deploy

ENV FLASK_APP /api/app.py 
EXPOSE 5000

CMD flask run --host=0.0.0.0