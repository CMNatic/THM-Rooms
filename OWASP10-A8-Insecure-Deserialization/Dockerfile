FROM ubuntu:20.04

MAINTANER CMNatic

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]