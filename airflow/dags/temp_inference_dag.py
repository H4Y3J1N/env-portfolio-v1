"""
Air Temperature Inference DAG

Runs inference for temperature prediction.

Schedule: Hourly
Output: 24-hour temperature forecast
"""

from datetime import datetime, timedelta


DAG_CONFIG = {
    'dag_id': 'air_temperature_inference',
    'description': 'Generate temperature predictions',
    'schedule_interval': '@hourly',
    'start_date': datetime(2024, 1, 1),
    'catchup': False,
    'tags': ['ml', 'inference', 'temperature']
}


class TemperatureInferenceDAG:
    """
    Temperature inference DAG.

    Tasks:
    1. fetch_latest_data - Get current sensor readings
    2. run_inference - Generate predictions
    3. send_predictions - Submit to dashboard API
    """

    def create_dag(self):
        """Create inference DAG."""
        pass

    def get_inference_command(self) -> str:
        return (
            "docker exec ml-worker python "
            "/opt/src/AirTemperature/inference.py"
        )
