#!/bin/bash
/usr/bin/python manage.py syncdb                   # Apply database migrations

# Start Gunicorn processes
echo Starting python manage.py runserver:8000.
exec /usr/bin/python manage.py runserver 0.0.0.0:8000
    "$@"
