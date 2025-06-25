FROM python:3.9-slim

# Install required OS packages
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 xvfb \
    chromium-driver chromium \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for headless Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV DISPLAY=:99

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run tests (headless)
CMD ["pytest", "tests/", "--html=reports/report.html", "--self-contained-html"]
