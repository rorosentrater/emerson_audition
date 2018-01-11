FROM robotgraves/pythonselenium:latest
LABEL authors='apaul@transparent.com,jnolette@transparent.com'

ADD requirements-cpython.txt /opt/requirements-cpython.txt

RUN opt/v/bin/pip install -U -r /opt/requirements-cpython.txt && \
    rm /opt/requirements-cpython.txt

ADD atest /opt/atest
ADD library /opt/library
WORKDIR /opt

CMD ["/opt/v/bin/python", "-m", "atest"]
