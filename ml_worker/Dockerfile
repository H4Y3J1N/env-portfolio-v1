# ML Worker Dockerfile
# GPU-enabled container for model training and inference

FROM nvidia/cuda:12.4.0-runtime-ubuntu22.04

# Set environment
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install Python and dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set Python alias
RUN ln -s /usr/bin/python3.10 /usr/bin/python

# Create working directories
WORKDIR /opt
RUN mkdir -p /opt/src /opt/data/model_artifacts

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Default command - idle for docker exec
CMD ["sleep", "infinity"]
