# ops-platform-api

Internal developer platform API for orchestrating cloud infrastructure and DevOps/SRE tools.

Built with Python, FastAPI, SQLAlchemy, and managed with [uv](https://docs.astral.sh/uv/).

## Integrated Providers

| Provider | Description |
|----------|-------------|
| AWS | Cloud infrastructure provisioning and management |
| Azure | Cloud infrastructure provisioning and management |
| Grafana Cloud | Monitoring and observability |
| Splunk | Log management and analytics |
| GitHub | Source code management and CI/CD |
| Jenkins | CI/CD pipeline management |
| GitLab | Source code management and CI/CD |

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Docker & Docker Compose (optional, for containerized development)

## Quick Start

```bash
# Install dependencies
uv sync

# Copy environment config
cp .env.example .env

# Run the development server
uv run uvicorn app.main:app --reload

# Open API docs
open http://localhost:8000/docs
```

## Development

```bash
# Install dev dependencies
uv sync --group dev

# Run tests
uv run pytest

# Run linter
uv run ruff check app/ tests/

# Run formatter
uv run ruff format app/ tests/

# Run type checker
uv run mypy app/
```

## Database Migrations

```bash
# Create a new migration
uv run alembic revision --autogenerate -m "description"

# Apply migrations
uv run alembic upgrade head

# Rollback one migration
uv run alembic downgrade -1
```

## Docker

```bash
# Start all services (API + PostgreSQL)
docker compose up -d

# View logs
docker compose logs -f api

# Stop all services
docker compose down
```

## Project Structure

```
app/
├── main.py              # Application entry point, lifespan events
├── core/                # Configuration, database, security, shared dependencies
├── models/              # SQLAlchemy ORM models
├── schemas/             # Pydantic request/response schemas
├── providers/           # External service API client wrappers
│   ├── base.py          # Abstract base provider with shared HTTP methods
│   ├── aws/             # AWS API client
│   ├── azure/           # Azure API client
│   ├── grafana/         # Grafana Cloud API client
│   ├── splunk/          # Splunk API client
│   ├── github/          # GitHub API client
│   ├── jenkins/         # Jenkins API client
│   └── gitlab/          # GitLab API client
├── api/v1/              # Versioned API routers (one per provider)
├── services/            # Business logic layer
└── middleware/           # Custom middleware (request logging, etc.)
```

## API

All provider endpoints are versioned under `/api/v1/{provider}/`.

- `GET /health` - Application health check
- `GET /api/v1/{provider}/status` - Provider status check
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)
