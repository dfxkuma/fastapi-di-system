import uvicorn
from app.env_validator import get_settings

settings = get_settings()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:server",
        host="0.0.0.0",
        port=settings.SERVER_PORT,
        reload=settings.APP_ENV == "development" or settings.APP_ENV == "testing",
    )
