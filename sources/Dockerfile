FROM python:3.5

    ENV PYTHONUNBUFFERED 1
#    RUN locale-gen en_US.UTF-8
#    ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

    RUN apt-get update && apt-get -y upgrade && apt-get -qqy install pdf2htmlex
    RUN apt-get install -y git python3-pip build-essential libssl-dev libffi-dev python3-dev curl
    RUN pip3 install --upgrade pip
    RUN apt-get install -y nodejs-legacy npm
    RUN npm install -g bower


    RUN mkdir /code
    WORKDIR /code/
    ADD . /code/
    RUN pip3 install -r requirements.txt
