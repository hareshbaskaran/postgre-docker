# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set proxy environment variables (if needed)
ENV http_proxy=http://proxy.example.com:8080
ENV https_proxy=http://proxy.example.com:8080

# Run the application
CMD ["fastapi", "main:app", "--host", "localhost", "--port", "8000"]
