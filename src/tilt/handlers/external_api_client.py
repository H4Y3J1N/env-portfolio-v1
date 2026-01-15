"""
External API Client

Handles authentication and requests to external services.
"""

from typing import Dict, Optional
import time


class ExternalAPIClient:
    """
    JWT-authenticated external API client.

    Features:
    - Automatic token refresh
    - Request retry logic
    - Rate limiting
    """

    def __init__(self, email: str, password: str, base_url: str):
        self.base_url = base_url
        self._token: Optional[str] = None
        self._token_expiry: float = 0

    def authenticate(self) -> bool:
        """Authenticate and obtain JWT token."""
        pass

    def _refresh_token_if_needed(self):
        """Refresh token if expired."""
        pass

    def get(self, endpoint: str, params: Dict = None) -> Dict:
        """Make authenticated GET request."""
        pass

    def post(self, endpoint: str, data: Dict) -> Dict:
        """Make authenticated POST request."""
        pass


def main():
    print("External API client skeleton")


if __name__ == '__main__':
    main()
