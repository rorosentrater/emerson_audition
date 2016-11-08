FROM ubuntu:latest
MAINTAINER apaul@transparent.com

RUN apt-get update && apt-get upgrade -y && apt-get install -y python-setuptools python-dev \
    build-essential libmysqlclient-dev firefox wget

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.10.0/geckodriver-v0.10.0-linux64.tar.gz -O /opt/geckodriver-v0.10.0-linux64.tar.gz
RUN tar -xzvf /opt/geckodriver-v0.10.0-linux64.tar.gz -C /bin
RUN rm /opt/geckodriver-v0.10.0-linux64.tar.gz

RUN apt-get install -y xvfb

ADD requirements-cpython.txt /opt/requirements-cpython.txt

RUN easy_install pip && pip install -U -r /opt/requirements-cpython.txt && \
    rm /opt/requirements-cpython.txt

# change this add based on project #
ADD test /opt/test
EXPOSE 8000
WORKDIR /opt/test

CMD ["echo", "$PATH"]