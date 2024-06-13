import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Settings class using Pydantic to manage application settings.

    Attributes:
    - DATABASE_URL: str - URL for connecting to the database.

    Configuration:
    - env_file: str - Optional configuration to load environment variables from a file (`.env` by default).
    """
    DATABASE_URL: str

    class Config:
        env_file = ".env"  # Load environment variables from .env file

settings = Settings()
