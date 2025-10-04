# Use Python 3.13 slim image (Debian-based, small footprint)
FROM python:3.13-slim

# Install build tools, BLAS/LAPACK, ngspice (required by PySpice), and cleanup in one layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        g++ \
        gfortran \
        pkg-config \
        libopenblas-dev \
        liblapack-dev \
        ngspice \
        libngspice0 \
        libngspice0-dev && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency files first (better layer caching)
COPY pyproject.toml poetry.lock* ./

# Install Poetry and dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the simulation script
COPY simulate_tl431_shunt.py .

# Default command: run the simulation
CMD ["python", "simulate_tl431_shunt.py"]

