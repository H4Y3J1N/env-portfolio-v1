"""
System Configuration Utilities

Configuration loading and management.
"""

from dataclasses import dataclass
from typing import Dict, Optional
import os


@dataclass
class SystemConfig:
    """System configuration."""

    # Location
    latitude: float = 35.0
    longitude: float = 127.0

    # GDD settings
    base_temperature: float = 10.0
    target_gdd: float = 1000.0

    # Panel limits
    min_tilt: float = 0.0
    max_tilt: float = 60.0

    # API settings
    api_base_url: str = ''
    api_timeout: int = 30

    @classmethod
    def from_yaml(cls, path: str) -> 'SystemConfig':
        """Load configuration from YAML file."""
        pass

    @classmethod
    def from_env(cls) -> 'SystemConfig':
        """Load configuration from environment variables."""
        return cls(
            latitude=float(os.getenv('LATITUDE', 35.0)),
            longitude=float(os.getenv('LONGITUDE', 127.0))
        )
