from pydantic_settings import BaseSettings

## Invoke BaseSettings to hand ENV variables and configure the app

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @classmethod
    def create_settings(cls):
        return cls()

