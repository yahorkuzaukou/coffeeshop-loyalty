FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile* ./

# Install dependencies using pipenv
RUN pipenv install --system --deploy

# Copy the application code
COPY src/ /app/src/
COPY deploy/ /app/deploy/

# Make entrypoint script executable
RUN chmod +x /app/deploy/entrypoint.sh && \
    ls -la /app/deploy/entrypoint.sh

# Expose the port the app runs on
EXPOSE 8000

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH=/app/src

# Use the entrypoint script
ENTRYPOINT ["/bin/bash", "/app/deploy/entrypoint.sh"]
