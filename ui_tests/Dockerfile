# ui_tests/Dockerfile
FROM selenium/standalone-chrome:latest

USER root

# Set environment vars (optional)
ENV PYTHONUNBUFFERED=1

# Install Python & pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy and install Python dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy test files
COPY . /app

# Run pytest test suite (modify test file name if needed)
CMD ["pytest", "test_dashboard.py"]
