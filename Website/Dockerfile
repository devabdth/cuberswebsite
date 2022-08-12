FROM python:3.8
MAINTAINER logs@cubersio.com

RUN apt-get update
RUN apt-get install -y nginx

COPY nginx.conf /etx/nginx

COPY . /srv/academy_app
WORKDIR /srv/academy_app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirments.txt --src /usr/local/src
RUN pip3 uwsgi

CMD service nginx start && uwsgi --ini uwsgi.ini
