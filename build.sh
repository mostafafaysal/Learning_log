#!/usr/bin/env bash
# Exit on error
set -o errexit

#!/bin/bash

# # Activate virtual environment
# source ll_env\Scripts\activate

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# python manage.py creatsu

# python manage.py createsuperuser --no-input --email=$DJANGO_SUPERUSER_EMAIL --username=$DJANGO_SUPERUSER_USERNAME --password=$DJANGO_SUPERUSER_PASSWORD

python manage.py createsuperuser --no-input --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --password $DJANGO_SUPERUSER_PASSWORD