FROM python:3.8

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    less vim \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/api
COPY . .
RUN pip install -r requirements.txt

CMD ["bash"]
