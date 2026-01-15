# Sensor Database Dockerfile
# PostgreSQL with TimescaleDB for time-series data

FROM timescale/timescaledb:latest-pg14

# Copy initialization scripts
COPY *.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_DB=sensor_data
