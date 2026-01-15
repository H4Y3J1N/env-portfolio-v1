"""
Operation Mode Utilities

Constants and utilities for operation modes.
"""

from enum import Enum


class OperationMode(Enum):
    """System operation modes."""
    CROP_PRIORITY = 'crop_priority'
    ENERGY_PRIORITY = 'energy_priority'
    BALANCED = 'balanced'
    MANUAL = 'manual'
    EMERGENCY = 'emergency'

    @classmethod
    def from_string(cls, mode_str: str) -> 'OperationMode':
        """Create from string value."""
        return cls(mode_str.lower())
