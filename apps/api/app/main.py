from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.users import router as users_router

app = FastAPI(
    title="LocalDrop API",
    version="0.1.0",
)


app.include_router(
    health_router,
    prefix="/api/v1",
)


app.include_router(
    users_router,
    prefix="/api/v1",
)