import httpx

from app.core.config import Settings
from app.providers.base import BaseProvider


class GitLabProvider(BaseProvider):
    provider_name = "gitlab"

    def __init__(self, client: httpx.AsyncClient, settings: Settings):
        super().__init__(client, base_url=settings.gitlab_api_url)
        self.settings = settings

    def _default_headers(self) -> dict[str, str]:
        return {
            **super()._default_headers(),
            "PRIVATE-TOKEN": self.settings.gitlab_token.get_secret_value(),
        }
