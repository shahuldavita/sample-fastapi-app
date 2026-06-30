from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Sample FastAPI App"
    DATABASE_URL: str = "postgresql://user:pass@localhost/db"
    SECRET_KEY: str = "changeme"

    class Config:
        env_file = ".env"

settings = Settings()
