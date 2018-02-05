#!/bin/bash

echo Starting Django site
exec python manage.py runserver 0.0.0.0:8000
