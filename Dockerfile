FROM ubuntu:20.04

RUN apt update
RUN apt-get -y install build-essential
RUN apt-get -y install git
RUN apt-get -y install python3
RUN git clone https://github.com/linglingec/FSE-Project-Team1
RUN cd FSE-Project-Team1; chmod +x build.sh test.sh; ./build.sh
