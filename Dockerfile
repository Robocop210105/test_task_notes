FROM python:3.11-slim

WORKDIR /src

COPY ./src /src
COPY requirements.txt /src/requirements.txt


RUN pip3 install -r /src/requirements.txt
