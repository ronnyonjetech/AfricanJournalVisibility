
# Use a stable Python base image
FROM python:3.11-slim

# Set environment variable to prevent buffering of output
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive




RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*


# Set working directory inside the container
WORKDIR /usr/src/BackEnd

# Copy the requirements.txt into the container
# COPY req/requirements.txt ./
COPY requirements.txt ./
# Upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install django-jazzmin if not in requirements.txt

RUN pip install django-jazzmin duckduckgo-search gunicorn
# Copy the rest of the application code into the container
COPY . /usr/src/BackEnd/

# Expose port 8000 for Django application
EXPOSE 8000



# Set default command to run the Django app with gunicorn
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]