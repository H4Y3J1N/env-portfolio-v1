## 프로젝트 개요

End-to-End MLOps 플랫폼입니다. 실시간 센서 데이터 처리, 시계열 예측, 자동화된 패널 최적화를 통합하여 작물 생장을 극대화하면서 태양 에너지 자원을 효율적으로 관리합니다.

### 주요 기능

- **시계열 예측**: Transformer 모델을 활용한 기온 및 일사량 예측
- **작물 생장 예측**: 다중 모델 앙상블 (LightGBM, LSTM, Transformer) 기반 수확량 추정
- **태양광 패널 틸트 최적화**: GDD(적산온도) 기반 자동 틸트 각도 제어
- **MLOps 파이프라인**: 자동화된 학습, 하이퍼파라미터 튜닝, 모델 배포
- **실시간 모니터링**: 예측 결과 및 시스템 상태 대시보드

## 시스템 아키텍처

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Docker Compose                              │
├─────────────┬─────────────┬─────────────┬─────────────┬─────────────┤
│   Airflow   │  ML Worker  │   MLflow    │ sams-admin  │  sensor-db  │
│   (DAGs)    │  (GPU/CUDA) │  (Tracking) │ (Dashboard) │ (PostgreSQL)│
├─────────────┴─────────────┴─────────────┴─────────────┴─────────────┤
│                        공유 볼륨                                     │
│              /opt/src (코드) | /opt/data (아티팩트)                   │
└─────────────────────────────────────────────────────────────────────┘
```

### 컴포넌트 구성

| 컴포넌트 | 설명 | 기술 스택 |
|---------|------|----------|
| **Airflow** | ML 파이프라인 워크플로우 오케스트레이션 | Apache Airflow, PostgreSQL |
| **ML Worker** | GPU 기반 모델 학습 및 추론 컨테이너 | PyTorch, CUDA 12.4, Python |
| **MLflow** | 실험 추적 및 모델 레지스트리 | MLflow, PostgreSQL |
| **sams-admin** | 관리자 대시보드 및 API 엔드포인트 | Flask, Redis |
| **sensor-db** | 시계열 센서 데이터 저장소 | PostgreSQL, TimescaleDB |

## ML 모델

### 1. 기온 예측 (`src/AirTemperature/`)

온실 내부 기온 예측을 위한 Transformer 기반 시계열 예측 모델

- **모델**: Positional Encoding이 적용된 커스텀 Transformer
- **입력 피처**: 외부 기상 데이터, 내부 센서 측정값
- **예측 범위**: 24시간 선행 예측

### 2. 일사량 예측 (`src/PvGen/`)

일사계 기반 태양 복사량 예측 모델

- **모델**: Attention 메커니즘이 적용된 Transformer 인코더
- **입력 피처**: 기상 예보, 과거 일사량 패턴
- **활용**: 태양광 패널 효율 최적화

### 3. 작물 생장 예측 (`src/crop/`)

작물 생육 단계 예측을 위한 다중 모델 앙상블

- **모델**: LightGBM, LSTM, Transformer
- **입력 피처**: 온도, 습도, 토양 수분, 광도
- **출력**: 생육 단계 분류 및 수확량 추정

### 4. 태양광 패널 틸트 제어 (`src/tilt/`)

GDD 기반 지능형 틸트 각도 최적화 시스템

- **알고리즘**: 작물 열 요구량을 위한 적산온도(GDD) 계산
- **운영 모드**: 작물 우선 / 에너지 우선 / 균형 모드
- **연동**: 모터 제어를 위한 PLC 명령 인터페이스

## 데이터 흐름

```
외부 센서 → sensor-db → Airflow DAG 트리거
                              ↓
                      ML Worker 실행
                              ↓
                MLflow 로깅 ← 학습/추론
                              ↓
                      sams-admin API
                              ↓
                    대시보드 / PLC 제어
```

## 기술 스택

- **오케스트레이션**: Apache Airflow 2.x
- **ML 프레임워크**: PyTorch 2.x, LightGBM
- **실험 추적**: MLflow
- **컨테이너화**: Docker, Docker Compose
- **GPU 지원**: NVIDIA CUDA 12.4
- **데이터베이스**: PostgreSQL
- **API**: Flask, Redis
- **언어**: Python 3.10+

## 프로젝트 구조

```
root/
├── airflow/
│   ├── config/              # Airflow 설정
│   └── dags/                # DAG 정의
│       └── utils/           # 공통 DAG 유틸리티
├── mlflow/
│   └── config/              # MLflow 서버 설정
├── ml_worker/               # GPU 워커 컨테이너
├── sams-admin/              # 관리자 대시보드
├── sensor-db/               # 데이터베이스
├── src/
│   ├── AirTemperature/      # 기온 예측 모듈
│   ├── PvGen/               # 일사량 예측 모듈
│   ├── crop/                # 작물 생장 예측 모듈
│   └── tilt/                # 틸트 최적화 모듈
│       ├── calculators/     # 핵심 계산 로직
│       ├── handlers/        # API 및 데이터 핸들러
│       ├── models/          # 데이터 모델
│       ├── scripts/         # 실행 스크립트
│       └── utils/           # 유틸리티 함수
└── docker-compose.yaml      # 서비스 오케스트레이션
```

## 시작하기

### 사전 요구사항

- Docker & Docker Compose
- NVIDIA GPU 및 CUDA 지원 (선택사항, GPU 가속용)
- 16GB 이상 RAM 권장

### 빠른 시작

```bash
# 모든 서비스 시작
docker-compose up -d

# UI 접속
# Airflow: http://localhost:8008
# MLflow: http://localhost:5000
# 대시보드: http://localhost:5001
```

## 개발 특징

- **모듈식 설계**: 각 ML 모듈을 독립적으로 배포 가능
- **설정 기반**: YAML 기반 설정으로 쉬운 커스터마이징
- **견고한 에러 처리**: Graceful degradation 및 재시도 메커니즘
- **확장 가능한 아키텍처**: 컨테이너 오케스트레이션을 통한 수평 확장 지원

## 라이선스

이 프로젝트는 포트폴리오 데모용입니다. 법적 문제가 생기지 않도록 최소한의 내용을 공개했습니다.

---
