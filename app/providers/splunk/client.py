import httpx

from app.core.config import Settings
from app.providers.base import BaseProvider


class SplunkProvider(BaseProvider):
    provider_name = "splunk"

    def __init__(self, client: httpx.AsyncClient, settings: Settings):
        super().__init__(client, base_url=settings.splunk_api_url)
        self.settings = settings

    def _default_headers(self) -> dict[str, str]:
        return {
            **super()._default_headers(),
            "Authorization": f"Bearer {self.settings.splunk_api_token.get_secret_value()}",
        }
