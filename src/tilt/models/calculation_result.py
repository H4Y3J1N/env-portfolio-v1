"""
Calculation Result Model

Data structure for tilt calculation results.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional


@dataclass
class CalculationResult:
    """Complete tilt calculation result."""

    # Angle outputs
    recommended_tilt: float
    recommended_azimuth: float

    # Metadata
    timestamp: datetime = field(default_factory=datetime.now)
    mode: str = 'balanced'
    confidence: float = 1.0

    # Input summary
    solar_altitude: Optional[float] = None
    current_gdd: Optional[float] = None
    target_gdd: Optional[float] = None

    # Decision factors
    factors: Dict = field(default_factory=dict)

    def to_dict(self) -> Dict:
        """Convert to dictionary for API submission."""
        return {
            'tilt': self.recommended_tilt,
            'azimuth': self.recommended_azimuth,
            'timestamp': self.timestamp.isoformat(),
            'mode': self.mode,
            'confidence': self.confidence
        }
