# File: ui_tests/Dockerfile
FROM python:3.10-slim

# Install required packages
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set environment vars for Selenium
ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER=/usr/bin/chromedriver \
    PYTHONUNBUFFERED=1

# Install Python deps
COPY ui_tests/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy tests
COPY ui_tests /app

CMD ["pytest", "test_dashboard.py"]
