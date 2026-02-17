import base64

import httpx

from app.core.config import Settings
from app.providers.base import BaseProvider


class JenkinsProvider(BaseProvider):
    provider_name = "jenkins"

    def __init__(self, client: httpx.AsyncClient, settings: Settings):
        super().__init__(client, base_url=settings.jenkins_url)
        self.settings = settings

    def _default_headers(self) -> dict[str, str]:
        credentials = f"{self.settings.jenkins_username}:{self.settings.jenkins_api_token.get_secret_value()}"
        encoded = base64.b64encode(credentials.encode()).decode()
        return {
            **super()._default_headers(),
            "Authorization": f"Basic {encoded}",
        }
