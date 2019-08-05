FROM python:3.7.0

RUN mkdir /mlflow/

RUN pip install --upgrade pip
RUN pip install mlflow>=1.1.0

CMD mlflow server \
    --backend-store-uri /mlflow \
    --host 0.0.0.0
