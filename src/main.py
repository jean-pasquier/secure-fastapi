from fastapi import FastAPI
from src.routers import items, security, users

app = FastAPI()

app.include_router(security.router)
app.include_router(users.router)
app.include_router(items.router)


@app.get("/health/", tags=["status"])
async def read_system_status():
    return {"status": "ok"}
