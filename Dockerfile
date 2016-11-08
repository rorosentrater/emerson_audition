FROM registry.transparent.com/qat-qat-base-image:latest
MAINTAINER apaul@transparent.com

ADD requirements-cpython.txt /opt/requirements-cpython.txt

RUN pip install -U -r /opt/requirements-cpython.txt && \
    rm /opt/requirements-cpython.txt

# change this add based on project #
ADD test /opt/test
EXPOSE 8000
WORKDIR /opt/test

CMD ["echo", "$PATH"]