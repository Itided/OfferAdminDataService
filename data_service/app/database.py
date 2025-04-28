from advanced_alchemy.config import AsyncSessionConfig
from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig
from advanced_alchemy.extensions.litestar import SQLAlchemyInitPlugin

from .settings import Settings


def sqlalchemy_plugin(settings: Settings):
    session_config = AsyncSessionConfig(expire_on_commit=False)
    sqlalchemy_config = SQLAlchemyAsyncConfig(
        connection_string=settings.db_dsn, session_config=session_config
    )
    return SQLAlchemyInitPlugin(config=sqlalchemy_config)
