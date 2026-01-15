# MLflow Server Dockerfile

FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Create artifact directory
RUN mkdir -p /opt/mlflow/artifacts

WORKDIR /opt/mlflow

# Expose MLflow UI port
EXPOSE 5000

# Start MLflow server
CMD ["mlflow", "server", \
     "--host", "0.0.0.0", \
     "--port", "5000", \
     "--default-artifact-root", "/opt/mlflow/artifacts"]
