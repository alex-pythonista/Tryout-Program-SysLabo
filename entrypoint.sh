#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate

echo "Loading initial data..."
python manage.py loaddata orgchart/fixtures/seed_data.json

# Start the Django development server
echo "Starting server..."
exec "$@"
