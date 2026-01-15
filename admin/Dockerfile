# Admin Dashboard Dockerfile

FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

WORKDIR /app

# Install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy application
COPY app.py /app/

EXPOSE 5001

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
