FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requerimientos.txt /code/
RUN pip install -r requerimientos.txt
COPY . /code/