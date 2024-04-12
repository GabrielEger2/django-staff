#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start Django app
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000