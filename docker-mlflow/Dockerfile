FROM continuumio/miniconda

WORKDIR /mlflow
ADD . /mlflow

RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential
RUN pip install --upgrade pip && \
    pip install -r dev-requirements.txt && \
    pip install mlflow>=1.1.0
