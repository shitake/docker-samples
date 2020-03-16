FROM python:3.8 AS py

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    less vim \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH /root/.poetry/bin:$PATH
RUN poetry completions bash > /etc/bash_completion.d/poetry.bash-completion \
    && poetry self update \
    && poetry config virtualenvs.in-project true --local
WORKDIR /poetry
