#!/bin/bash

echo Starting Django site
echo Running at http://127.0.0.1:8000
exec python manage.py runserver 0.0.0.0:8000
