#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Database is ready!"

# Run migrations
# echo "Running migrations..."
# alembic upgrade head

# Start the application
echo "Starting application..."
exec python -m main