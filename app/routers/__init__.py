from fastapi import FastAPI
from . import health

app = FastAPI(title="Artificial Intelligence", description="7th Semester project")

app.include_router(health.router, prefix="/health", tags=["Health"])
