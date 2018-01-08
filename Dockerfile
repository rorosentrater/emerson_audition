FROM robotgraves/virtualpython
MAINTAINER apaul@transparent.com

# LIBS
RUN apt-get update && apt-get install -y bzip2 \
    zlib1g-dev libopenjpeg-dev libjpeg-dev xvfb

# FIREFOX
ARG FIREFOX_VERSION=57.0
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && wget -O /tmp/firefox.tar.bz2 https://download-installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-US/firefox-$FIREFOX_VERSION.tar.bz2 \
  && rm -rf /opt/firefox \
  && tar -C /opt -xjf /tmp/firefox.tar.bz2 \
  && rm /tmp/firefox.tar.bz2 \
  && mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \
  && ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox

# GECKODRIVER
ARG GECKODRIVER_VERSION=0.19.1
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
  && rm -rf /opt/geckodriver \
  && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
  && rm /tmp/geckodriver.tar.gz \
  && mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \
  && chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \
  && ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver

# PROJECT REQUIREMENTS
ADD requirements-cpython.txt /opt/requirements-cpython.txt
RUN opt/v/bin/pip install -U -r /opt/requirements-cpython.txt && \
    rm /opt/requirements-cpython.txt

ADD atest /opt/atest
ADD library /opt/library
EXPOSE 8000
WORKDIR /opt

CMD ["/opt/v/bin/python", "-m", "atest"]
