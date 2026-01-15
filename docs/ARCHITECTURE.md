# Architecture Documentation

## System Overview

This is a microservices-based MLOps platform designed for agricultural IoT applications.

## Component Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                              SAMS Platform                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐               │
│  │   External   │    │   Sensor     │    │   Weather    │               │
│  │   Sensors    │───▶│   Database   │◀───│   API        │               │
│  └──────────────┘    └──────┬───────┘    └──────────────┘               │
│                             │                                            │
│                             ▼                                            │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                        Apache Airflow                             │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐    │   │
│  │  │ Temp    │ │ PvGen   │ │ Crop    │ │ Tilt    │ │ Data    │    │   │
│  │  │ DAG     │ │ DAG     │ │ DAG     │ │ DAG     │ │ Ingest  │    │   │
│  │  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └─────────┘    │   │
│  └───────┼──────────┼──────────┼──────────┼────────────────────────┘   │
│          │          │          │          │                             │
│          ▼          ▼          ▼          ▼                             │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                         ML Worker (GPU)                           │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐             │   │
│  │  │ Temp     │ │ PvGen    │ │ Crop     │ │ Tilt     │             │   │
│  │  │ Model    │ │ Model    │ │ Models   │ │ Optimizer│             │   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘             │   │
│  └──────────────────────────────────────┬───────────────────────────┘   │
│                                         │                               │
│          ┌──────────────────────────────┼───────────────────────┐       │
│          │                              ▼                       │       │
│          │  ┌──────────────┐    ┌──────────────┐               │       │
│          │  │   MLflow     │    │  sams-admin  │               │       │
│          │  │   Server     │    │  Dashboard   │               │       │
│          │  └──────────────┘    └──────┬───────┘               │       │
│          │                             │                        │       │
│          └─────────────────────────────┼────────────────────────┘       │
│                                        │                                │
│                                        ▼                                │
│                               ┌──────────────┐                          │
│                               │  PLC / Motor │                          │
│                               │  Controller  │                          │
│                               └──────────────┘                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## Data Flow

1. **Data Ingestion**: Sensors → sensor-db
2. **Processing**: Airflow triggers data processing DAGs
3. **Training**: ML Worker executes training scripts
4. **Tracking**: MLflow logs experiments and artifacts
5. **Inference**: Scheduled predictions via Airflow
6. **Action**: Tilt commands sent to PLC controller

## Technology Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Orchestration | Airflow | Industry standard, DAG visualization |
| ML Framework | PyTorch | Flexibility, research-friendly |
| Experiment Tracking | MLflow | Model versioning, artifact management |
| Container Runtime | Docker | Portability, GPU support |
| Time-series DB | TimescaleDB | PostgreSQL compatibility, performance |
