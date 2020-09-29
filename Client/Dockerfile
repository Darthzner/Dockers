FROM ubuntu

WORKDIR /Spark
EXPOSE 5269
EXPOSE 5443
EXPOSE 5280
EXPOSE 5222
EXPOSE 9090

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -yqq update \
&&  apt-get -yqq upgrade
RUN apt install -yqq build-essential && apt install -yqq dpkg \
&& apt install -yqq wget \
&& wget https://download.igniterealtime.org/spark/dailybuilds/spark_2_9_3-20200928.deb
RUN dpkg -i spark_2_9_3-20200928.deb
RUN DEBIAN_FRONTEND="noninteractive" apt install -yqq default-jre

ENV PATH="/opt/spark/bin:${PATH}"

ENTRYPOINT ["Spark"]

