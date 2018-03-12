FROM ubuntu:latest

RUN useradd -ms /bin/bash docker \
  && echo "docker:docker" | chpasswd \
  && adduser docker sudo

USER docker

WORKDIR /home/docker/AptGetInstallTest

ADD . /home/docker/AptGetInstallTest

USER root

RUN echo "root:Docker!" | chpasswd

RUN apt-get update \
  && apt-get -y install sudo \
  && apt-get install -y python3-pip python3-dev \
  && pip3 install --upgrade pip \
  && pip3 install -r requirements.txt

USER docker

ENV PYTHONPATH $PYTHONPATH:/AptGetInstallTest

# Run test cases when the container launches
CMD pytest TestSuites/TestAptGetInstall.py -v
