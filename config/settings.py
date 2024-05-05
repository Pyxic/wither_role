from typing import List

from pydantic_settings import BaseSettings
from starlette.templating import Jinja2Templates
from yarl import URL


class Settings(BaseSettings):
    # Variables for the repository
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_echo: bool = False

    cors_origin_whitelist: List = ["*"]
    secret_key: str

    # Secret key for signing jwt tokens
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_refresh_expiration: int = 60 * 60 * 24 * 30  # 30 days
    jwt_access_expiration: int = 60 * 60  # 1 hour

    @property
    def db_url(self) -> str:
        """
        Assemble repository URL from settings.

        :return: repository URL.

        """
        url = str(URL.build(
            scheme="postgresql+asyncpg",
            host=self.postgres_host,
            port=self.postgres_port,
            user=self.postgres_user,
            password=self.postgres_password,
            path=f"/{self.postgres_db}",
        ))
        print(url)
        return url

    class Config:
        """
        Configure the application.
        """

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

templates = Jinja2Templates(directory="templates")
