
# Use official Python image
FROM python:3

# Set environment variable to prevent buffering of output
ENV PYTHONUNBUFFERED=1

# Install system dependencies, including Rust for compiling safetensors
RUN apt-get update && apt-get install -y \
    build-essential \
    meson \
    ninja-build \
    pkg-config \
    libc6-dev \
    libatlas-base-dev \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Rust using rustup
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Set Rust environment variables
ENV PATH="/root/.cargo/bin:${PATH}"

# Set working directory inside the container
WORKDIR /usr/src/BackEnd

# Copy the requirements.txt into the container
COPY req/requirements.txt ./

# Upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install django-jazzmin if not in requirements.txt
RUN pip install django-jazzmin

# Copy the rest of the application code into the container
COPY . /usr/src/BackEnd/

# Expose port 8000 for Django application
EXPOSE 8000

