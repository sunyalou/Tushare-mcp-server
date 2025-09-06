import os
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    tushare_token: str = ""
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()