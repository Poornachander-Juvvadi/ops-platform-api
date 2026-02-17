from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    app_name: str = "ops-platform-api"
    app_version: str = "0.1.0"
    debug: bool = False
    log_level: str = "info"

    # Database
    database_url: str = "sqlite+aiosqlite:///./ops_platform.db"

    # Security
    secret_key: SecretStr = SecretStr("change-me-in-production")
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 30

    # AWS
    aws_region: str = "us-east-1"
    aws_access_key_id: SecretStr = SecretStr("")
    aws_secret_access_key: SecretStr = SecretStr("")
    aws_api_base_url: str = ""

    # Azure
    azure_tenant_id: str = ""
    azure_client_id: str = ""
    azure_client_secret: SecretStr = SecretStr("")
    azure_subscription_id: str = ""
    azure_api_base_url: str = ""

    # Grafana Cloud
    grafana_api_url: str = ""
    grafana_api_key: SecretStr = SecretStr("")

    # Splunk
    splunk_api_url: str = ""
    splunk_api_token: SecretStr = SecretStr("")

    # GitHub
    github_api_url: str = "https://api.github.com"
    github_token: SecretStr = SecretStr("")

    # Jenkins
    jenkins_url: str = ""
    jenkins_username: str = ""
    jenkins_api_token: SecretStr = SecretStr("")

    # GitLab
    gitlab_api_url: str = "https://gitlab.com/api/v4"
    gitlab_token: SecretStr = SecretStr("")

    # HTTP Client
    http_client_timeout: int = 30
    http_client_max_connections: int = 100


@lru_cache
def get_settings() -> Settings:
    return Settings()
