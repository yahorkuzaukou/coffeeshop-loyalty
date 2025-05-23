FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile* ./

# Install dependencies using pipenv
RUN pipenv install --system --deploy

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH=/app/src

# Command to run the application
CMD ["python", "-m", "main"] 