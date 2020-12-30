#!/usr/bin/env bash
echo "Starting application"

cd /home/shubham/Desktop/Projects/django_projects/myTextUtils

echo "now in project directory"

echo "now going to activate virtual env"

source ../django_env/bin/activate

echo "virtual env is activated"

python3 manage.py runserver
