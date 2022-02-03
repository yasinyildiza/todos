__version__ = "0.0.1"

import fastapi

from .routers.v1 import items, users

app = fastapi.FastAPI()

@app.get("/health")
def health():
    return {"success": True}

app.include_router(items.router, prefix="/api/v1/items", tags=["item"])
app.include_router(users.router, prefix="/api/v1/users", tags=["user"])
