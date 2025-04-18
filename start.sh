#!/usr/bin/env bash
# Exit on error
set -o errexit

# Run migrations
python manage.py migrate

# Start the server
gunicorn vj_project.wsgi:application