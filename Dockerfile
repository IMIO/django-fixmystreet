#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
FROM ubuntu:14.04
MAINTAINER Benoît Suttor <bsuttor@imio.com>


RUN \
  apt-get update && \
  apt-get install -y python-dev python-virtualenv libgeos-3.4.2 libgdal1h make gcc nodejs npm curl libpq-dev

RUN mkdir -p /opt/fixmystreet
WORKDIR /opt/fixmystreet
ADD . /opt/fixmystreet/
RUN make develop

COPY ./docker-entrypoint.sh /opt/fixmystreet/docker-entrypoint.sh
#ENTRYPOINT ["/opt/fixmystreet/docker-entrypoint.sh"]