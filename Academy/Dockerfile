FROM python:3.8

RUN apt-get update
RUN apt-get install -y nginx

COPY nginx.conf /etc/nginx

COPY . /srv/flask_app
WORKDIR /srv/flask_app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --src /usr/local/src
RUN pip3 install uwsgi

CMD service nginx start && uwsgi --ini uwsgi.ini