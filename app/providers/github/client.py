import httpx

from app.core.config import Settings
from app.providers.base import BaseProvider


class GitHubProvider(BaseProvider):
    provider_name = "github"

    def __init__(self, client: httpx.AsyncClient, settings: Settings):
        super().__init__(client, base_url=settings.github_api_url)
        self.settings = settings

    def _default_headers(self) -> dict[str, str]:
        return {
            **super()._default_headers(),
            "Authorization": f"Bearer {self.settings.github_token.get_secret_value()}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
