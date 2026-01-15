"""
GDD Calculation Model

Data structures for Growing Degree Days calculations.
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class GDDCalculation:
    """GDD calculation record."""

    date: date
    min_temperature: float
    max_temperature: float
    base_temperature: float
    daily_gdd: float
    accumulated_gdd: float
    method: str = 'simple'

    @classmethod
    def calculate(
        cls,
        date_val: date,
        min_temp: float,
        max_temp: float,
        base_temp: float = 10.0,
        accumulated: float = 0.0
    ) -> 'GDDCalculation':
        """Calculate GDD from temperature data."""
        avg_temp = (min_temp + max_temp) / 2
        daily = max(0, avg_temp - base_temp)

        return cls(
            date=date_val,
            min_temperature=min_temp,
            max_temperature=max_temp,
            base_temperature=base_temp,
            daily_gdd=daily,
            accumulated_gdd=accumulated + daily
        )
