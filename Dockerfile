FROM ubuntu:latest

WORKDIR /AptGetInstallTest

ADD . /AptGetInstallTest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && pip3 install --upgrade pip \
  && pip3 install -r requirements.txt

EXPOSE 80

ENV PYTHONPATH $PYTHONPATH:/AptGetInstallTest

# Run test cases when the container launches
CMD pybot -s TestSuites --outputdir Results TestSuites
