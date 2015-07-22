#!/bin/bash
/usr/bin/python manage.py syncdb                   # Apply database migrations
/usr/bin/python manage.py makemigrations
# Start Gunicorn processes
echo Starting python manage.py runserver on port 8000.
exec /usr/bin/python manage.py runserver 0.0.0.0:8000
    "$@"
