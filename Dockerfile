FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    pytest

COPY . .
