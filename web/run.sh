#!/bin/bash

sleep 5
python3.6 manage.py migrate
python3.6 manage.py collectstatic --noinput
echo Starting Gunicorn
exec /usr/local/bin/gunicorn stockCRM.wsgi:application -w 2 -b :8000

