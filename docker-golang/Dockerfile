FROM ubuntu:20.04

ENV USER=shitake
ENV GROUP=shitake
RUN useradd -m ${USER}

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV TZ Asia/Tokyo

ENV GOVER 1.15.6
ENV INSTALL_DIR /usr/local
ENV GOROOT ${INSTALL_DIR}/go
ENV GOPATH /root/.go

RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
        ca-certificates \
        git \
        vim \
        wget \
    && rm -rf /var/lib/apt/lists/*

# Install Go
WORKDIR /usr/local

RUN wget https://golang.org/dl/go${GOVER}.linux-amd64.tar.gz \
    && tar -C ${INSTALL_DIR} -xzf go${GOVER}.linux-amd64.tar.gz \
    && rm go${GOVER}.linux-amd64.tar.gz
ENV PATH $PATH:${GOROOT}/bin
WORKDIR ${GOPATH}

WORKDIR /app

USER ${USER}:${GROUP}

CMD ["/bin/bash"]
