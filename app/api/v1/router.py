from fastapi import APIRouter

from app.api.v1 import aws, azure, github, gitlab, grafana, jenkins, splunk

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(aws.router)
v1_router.include_router(azure.router)
v1_router.include_router(grafana.router)
v1_router.include_router(splunk.router)
v1_router.include_router(github.router)
v1_router.include_router(jenkins.router)
v1_router.include_router(gitlab.router)
