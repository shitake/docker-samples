FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt update
RUN apt install -y \
  git \
  make \
  nginx \
  python3-pip \
  sudo \
  vim \
  wget \
  zip \
  || true

# Pyenv
RUN apt install -y \
  gcc \
  make \
  libssl-dev \
  libbz2-dev \
  libreadline-dev \
  libsqlite3-dev \
  zlib1g-dev

# MeCab
RUN apt install -y \
  libmecab-dev \
  mecab \
  mecab-ipadic-utf8 \
  swig

# Locale
RUN apt install -y \
  language-pack-ja-base \
  language-pack-ja
RUN update-locale LANG=ja_JP.UTF-8

# Pyenv
RUN \
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && \
  echo 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
ENV PATH $PATH:/root/.pyenv/bin
# Install Python
RUN pyenv install 3.6.6
RUN pyenv global 3.6.6
RUN pyenv rehash
ENV PATH $PATH:/root/.pyenv/shims
RUN python -V

# Install Pipenv
RUN pip install --upgrade pip
RUN pip install pipenv -U
RUN mkdir /home/sandbox
WORKDIR /home/sandbox
COPY Pipfile .
# COPY Pipfile.lock .
RUN pipenv install --skip-lock

# Jupyter
# COPY jupyter_notebook_config.py /.jupyter/jupyter_notebook_config.py
COPY docker/entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh]
