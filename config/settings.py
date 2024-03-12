from pydantic_settings import BaseSettings
from yarl import URL


class Settings(BaseSettings):
    # Variables for the repository
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_echo: bool = False

    @property
    def db_url(self) -> URL:
        """
        Assemble repository URL from settings.

        :return: repository URL.

        """
        return URL.build(
            scheme="postgres+asyncpg",
            host=self.postgres_host,
            port=self.postgres_port,
            user=self.postgres_user,
            password=self.postgres_password,
            path=f"/{self.postgres_db}",
        )

settings = Settings()
