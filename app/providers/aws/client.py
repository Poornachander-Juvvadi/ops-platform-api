import httpx

from app.core.config import Settings
from app.providers.base import BaseProvider


class AWSProvider(BaseProvider):
    provider_name = "aws"

    def __init__(self, client: httpx.AsyncClient, settings: Settings):
        super().__init__(client, base_url=settings.aws_api_base_url)
        self.settings = settings

    def _default_headers(self) -> dict[str, str]:
        return {
            **super()._default_headers(),
            "X-AWS-Region": self.settings.aws_region,
        }
