FROM ubuntu
WORKDIR /Polymorph1

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -yqq update
RUN apt install -yqq python3-pip
RUN apt-get -yqq install build-essential python-dev libnetfilter-queue-dev tshark tcpdump python3-pip wireshark git net-tools iptables 
RUN apt-get install -yqq vim
RUN pip3 install git+https://github.com/kti/python-netfilterqueue
RUN git clone https://github.com/shramos/polymorph 

RUN cd polymorph && ls && python3 setup.py install


ENTRYPOINT ["polymorph"]


