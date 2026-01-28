import uvicorn
from fastapi import FastAPI
from src.routes.api import router as api_router

app = FastAPI(title="PoC Cloud Run & Storage", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    # La configuración de host 0.0.0.0 y puerto es vital para Cloud Run
    import os
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)