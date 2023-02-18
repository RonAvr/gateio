FROM python:3.10.1-slim-buster AS builder

WORKDIR /
RUN apt-get update \
    && apt-get -y install libpq-dev gcc curl unzip git
ARG SSH_KEY
RUN pip install pipenv
COPY Pipfile Pipfile.lock /
COPY app/ /app/
RUN export PIPENV_VENV_IN_PROJECT=1 && pipenv sync
ENV PATH=/.venv/bin:$PATH
EXPOSE 5002

CMD uvicorn app.main:app --host 0.0.0.0 --port 5002