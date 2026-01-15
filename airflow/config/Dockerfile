# Airflow Dockerfile
# Apache Airflow with custom dependencies

FROM apache/airflow:2.8.1-python3.10

USER root

# Install system dependencies
RUN apt-get update && apt-get install -y \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy DAGs
COPY dags/ /opt/airflow/dags/
