FROM python:3.8.1-slim as py
RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
        curl less vim
RUN pip install \
        pytest \
        testinfra
