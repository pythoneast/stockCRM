FROM python:3.6 as dev
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y gettext
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt
ADD . /usr/src/app

FROM dev as prod
RUN pip3 install gevent gunicorn
ENTRYPOINT ["sh", "/usr/src/app/run.sh"]

