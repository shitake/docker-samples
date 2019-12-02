FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

# Install basic dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    sudo git curl wget cmake vim gcc g++ build-essential ca-certificates software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Install Python
RUN add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y python3.6 \
    && apt-get install python3-pip -y
RUN ln -s /usr/bin/python3.6 /usr/local/bin/python3 \
    && ln -s /usr/bin/python3.6 /usr/local/bin/python \
    && ln -s /usr/bin/pip3 /usr/local/bin/pip \
    && pip install --upgrade pip

# Install common Python packages
ADD ./requirements.txt /tmp
RUN pip install setuptools -U && pip install -r /tmp/requirements.txt && pip install -U tensorflow tensorflow-gpu torch torchvision

# Set working directory
WORKDIR /home/sandbox

# Config and clean up
RUN ldconfig \
    && apt-get clean \
    && apt-get autoremove

CMD ["/bin/bash", "docker/entrypoint.sh"]
