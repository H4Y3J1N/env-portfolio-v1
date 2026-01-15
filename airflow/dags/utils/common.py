"""
Common DAG Utilities

Shared functions for SAMS Airflow DAGs.
"""

from typing import Dict, List, Optional


def get_docker_exec_command(
    container: str,
    script_path: str,
    env_vars: Optional[Dict[str, str]] = None
) -> str:
    """
    Generate docker exec command for ml-worker.

    Args:
        container: Target container name
        script_path: Path to Python script in container
        env_vars: Environment variables to pass

    Returns:
        Complete docker exec command string
    """
    cmd_parts = ['docker', 'exec']

    if env_vars:
        for key, value in env_vars.items():
            cmd_parts.extend(['-e', f'{key}={value}'])

    cmd_parts.extend([container, 'python', script_path])
    return ' '.join(cmd_parts)


def load_dag_config(config_path: str) -> Dict:
    """Load DAG configuration from YAML file."""
    # Implementation would load and parse YAML
    return {}


def get_default_args() -> Dict:
    """Get default DAG arguments."""
    return {
        'owner': 'sams',
        'depends_on_past': False,
        'retries': 1,
        'retry_delay_minutes': 5
    }
