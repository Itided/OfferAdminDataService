from typing import Literal

from granian.log import LogLevels
from pydantic import Secret
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from sqlalchemy.engine.url import URL


class Settings(BaseSettings):
    debug: bool = False
    log_level: LogLevels = LogLevels.info
    app_port: int = 5000

    db_driver: str = "postgresql+asyncpg"

    db_host: SecretStr
    db_name: SecretStr
    db_user: SecretStr
    db_port: SecretStr
    db_password: SecretStr

    db_name_dev: SecretStr
    db_host_dev: SecretStr
    db_port_dev: SecretStr
    db_user_dev: SecretStr
    db_password_dev: SecretStr

    environment: Literal["production", "development"] = "development"

    @property
    def db_dsn(self) -> URL:
        if self.environment == "development":
            return URL.create(
                self.db_driver,
                self.db_user_dev.get_secret_value(),
                self.db_password_dev.get_secret_value(),
                self.db_host_dev.get_secret_value(),
                int(self.db_port_dev.get_secret_value()),
                self.db_name_dev.get_secret_value(),
            )

        return URL.create(
            self.db_driver,
            self.db_user.get_secret_value(),
            self.db_password.get_secret_value(),
            self.db_host.get_secret_value(),
            int(self.db_port.get_secret_value()),
            self.db_name.get_secret_value(),
        )


settings = Settings()
