-- Sensor Database Schema
-- Time-series data storage for agricultural sensors

-- Enable TimescaleDB extension
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Sensor readings table
CREATE TABLE IF NOT EXISTS sensor_readings (
    time TIMESTAMPTZ NOT NULL,
    sensor_id VARCHAR(50) NOT NULL,
    sensor_type VARCHAR(50) NOT NULL,
    value DOUBLE PRECISION NOT NULL,
    unit VARCHAR(20),
    quality_flag INTEGER DEFAULT 0,
    location VARCHAR(100)
);

-- Convert to hypertable for time-series optimization
SELECT create_hypertable('sensor_readings', 'time', if_not_exists => TRUE);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_sensor_id ON sensor_readings (sensor_id, time DESC);
CREATE INDEX IF NOT EXISTS idx_sensor_type ON sensor_readings (sensor_type, time DESC);

-- GDD tracking table
CREATE TABLE IF NOT EXISTS gdd_daily (
    date DATE PRIMARY KEY,
    min_temp DOUBLE PRECISION NOT NULL,
    max_temp DOUBLE PRECISION NOT NULL,
    daily_gdd DOUBLE PRECISION NOT NULL,
    accumulated_gdd DOUBLE PRECISION NOT NULL,
    base_temp DOUBLE PRECISION DEFAULT 10.0
);

-- Prediction results table
CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    model_type VARCHAR(50) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    target_time TIMESTAMPTZ NOT NULL,
    predicted_value DOUBLE PRECISION NOT NULL,
    confidence DOUBLE PRECISION,
    model_version VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_predictions_model ON predictions (model_type, timestamp DESC);
