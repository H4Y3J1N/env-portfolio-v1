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
    latitude: float = 1.0
    longitude: float = 1.0

    # GDD settings
    base_temperature: float = 1.0
    target_gdd: float = 1.0

    # Panel limits
    min_tilt: float = 0.0
    max_tilt: float = 1.0

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
            latitude=float(os.getenv('LATITUDE', 1.0)),
            longitude=float(os.getenv('LONGITUDE', 1.0))
        )
