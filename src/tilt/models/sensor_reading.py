"""
Sensor Reading Model

Data structure for sensor measurements.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class SensorReading:
    """Individual sensor reading."""

    sensor_id: str
    timestamp: datetime
    value: float
    unit: str
    quality: int = 0  # 0=good, 1=warning, 2=error

    # Optional metadata
    location: Optional[str] = None
    sensor_type: Optional[str] = None

    def is_valid(self) -> bool:
        """Check if reading is valid."""
        return self.quality == 0
