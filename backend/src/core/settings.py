from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    APP_HOST: str = Field(default="0.0.0.0")
    APP_PORT: int = Field(default=8000)

    DB_HOST: str = Field(default="localhost")
    DB_DRIVER: str = Field(default="postgresql+asyncpg")
    DB_PORT: int = Field(default=5432)
    DB_USER: str = Field(default="postgres")
    DB_PASSWORD: str = Field(default="postgres")
    DB_NAME: str = Field(default="postgres")

    @property
    def DATABASE_URL(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        populate_by_name = True
        extra = "ignore"

settings = Settings()